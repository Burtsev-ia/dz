from typing import List, Tuple, Dict, Union
from .memory import PixelMemory


class Evaluator:
    def __init__(self, memory: PixelMemory):
        self.memory = memory

    def run_benchmark(
        self,
        sequence: List[Tuple[str, Union[str, Tuple[str, str]]]],
        check_points: List[int] = None,
        verbose: bool = False
    ) -> Dict[int, float]:
        results = {}
        query_count = 0
        total_learned = 0
        
        query_results = []
        
        for idx, (item_type, content) in enumerate(sequence):
            if item_type == "fact":
                self.memory.learn(content)
                total_learned += 1
                if verbose:
                    print(f"[{idx+1:03d}] LEARN: {content[:60]}")
                
            elif item_type == "query":
                question, expected = content
                result = self.memory.query(question)
                
                correct = self._is_correct_match(expected, result[0] if result else "")
                query_results.append(correct)
                query_count += 1
                
                if verbose:
                    returned = result[0] if result else "I forgot that(("
                    status = "[OK]" if correct else "[FAIL]"
                    print(f"[{idx+1:03d}] QUERY: {question}")
                    print(f"       -> {returned} {status}")
                
                accuracy = sum(query_results) / len(query_results)
                
                if check_points and (idx + 1) in check_points:
                    results[idx + 1] = accuracy
                    print(f"Step {idx + 1}: {total_learned} facts, {query_count} queries, Accuracy = {accuracy:.2%}")
        
        final_accuracy = sum(query_results) / len(query_results) if query_results else 0.0
        if query_results:
            results[len(sequence)] = final_accuracy
        
        return results, query_results

    def run_fixed_checkpoints(
        self,
        facts: List[str],
        qa_pairs: List[Tuple[str, str]],
        check_points: List[int]
    ) -> Dict[int, float]:
        results = {}
        
        fact_idx = 0
        for checkpoint in sorted(check_points):
            facts_to_learn = checkpoint - fact_idx
            for _ in range(facts_to_learn):
                if fact_idx < len(facts):
                    self.memory.learn(facts[fact_idx])
                    fact_idx += 1
            
            correct = 0
            for question, expected in qa_pairs:
                result = self.memory.query(question)
                if result and self._is_correct_match(expected, result[0]):
                    correct += 1
            
            accuracy = correct / len(qa_pairs) if qa_pairs else 0.0
            results[checkpoint] = accuracy
            print(f"After {checkpoint} facts: Accuracy = {accuracy:.2%}")
        
        return results

    def _is_correct_match(self, expected: str, returned: str) -> bool:
        import re
        cleaned = re.sub(r'\*\*', '', returned).lower().strip()
        expected_lower = expected.lower().strip()
        
        if not expected_lower or not cleaned:
            return False
        
        return expected_lower in cleaned or cleaned in expected_lower

    def run_interactive(self, facts: List[str], queries: List[str]):
        print("\n=== Pixel's Memory Demo ===\n")
        
        for idx, fact in enumerate(facts):
            self.memory.learn(fact)
            print(f"Learned: {fact}")
        
        print(f"\nMemory now holds {len(self.memory)} facts\n")
        
        for query in queries:
            print(f"Query: {query}")
            result = self.memory.query(query)
            if result:
                fact, keywords, score = result
                print(f"  → {fact}")
                print(f"    (matched: {keywords}, similarity: {score:.2f})")
            else:
                print("  → No match found")
            print()

    def get_memory_state(self) -> List[Dict]:
        state = []
        for item in self.memory.items:
            state.append({
                'fact': item.fact,
                'keywords': item.keywords,
                'access_count': item.access_count,
                'importance': item.compute_importance()
            })
        return state