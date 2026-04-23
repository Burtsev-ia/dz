#!/usr/bin/env python3
"""Frequency-based memory test - 30 unique facts with varied occurrences."""

from pixel_memory import PixelMemory, Evaluator
import random


def generate_test_data():
    random.seed(42)
    
    # 30 Unique facts - mix of owner, trivia, and random
    # 15 owner facts, 10 trivia facts, 5 random facts
    unique_facts = [
        # Owner facts (15)
        "My owner name is Sarah",
        "My favorite food is pizza",
        "My owner works as a doctor",
        "My owner birthday is March 15th",
        "My owner lives in New York City",
        "My owner favorite color is purple",
        "My owner has a cat named Whiskers",
        "My owner loves reading mystery novels",
        "My owner drives a blue Honda",
        "My owner plays guitar on weekends",
        "My owner favorite season is autumn",
        "My owner speaks three languages",
        "My owner favorite holiday is Christmas",
        "My owner adopted me from a shelter",
        "My owner is allergic to peanuts",
        
        # Trivia/Scientific facts (10)
        "The sky is blue",
        "Water freezes at zero degrees",
        "Cats have four legs",
        "The sun is a star",
        "Dogs are mammals",
        "The moon orbits the Earth",
        "Birds can fly",
        "Fish live in water",
        "The Earth orbits the sun",
        "Rain comes from clouds",
        
        # Random/Dog facts (5)
        "I love chasing butterflies",
        "My favorite toy is a squeaky ball",
        "I sleep on a soft dog bed",
        "My fur is golden and white",
        "I enjoy walks in the park",
    ]
    
    # Occurrence distribution: 127 total
    # 5 facts × 2 = 10
    # 7 facts × 3 = 21
    # 5 facts × 4 = 20
    # 5 facts × 5 = 25
    # 5 facts × 6 = 30
    # 3 facts × 7 = 21
    
    occurrence_map = {
        0: 2, 1: 2, 2: 2, 3: 2, 4: 2,           # 5 facts × 2
        5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3,  # 7 facts × 3
        12: 4, 13: 4, 14: 4, 15: 4, 16: 4,      # 5 facts × 4
        17: 5, 18: 5, 19: 5, 20: 5, 21: 5,      # 5 facts × 5
        22: 6, 23: 6, 24: 6, 25: 6, 26: 6,      # 5 facts × 6
        27: 7, 28: 7, 29: 7,                    # 3 facts × 7
    }
    
    # Build fact list with occurrences
    fact_sequence = []
    for fact_idx, occurrences in occurrence_map.items():
        for _ in range(occurrences):
            fact_sequence.append(unique_facts[fact_idx])
    
    random.shuffle(fact_sequence)
    
    # Query distribution: now matches occurrence_map (127 total)
    # Each fact is queried as many times as it occurs
    
    query_count_map = occurrence_map.copy()  # Query count = occurrence count
    
    # Create queries for each unique fact
    queries_by_fact = {}
    for fact_idx in range(30):
        q_count = query_count_map[fact_idx]
        fact = unique_facts[fact_idx]
        # Create question from fact
        q = fact_to_question(fact)
        queries_by_fact[fact_idx] = [(q, fact) for _ in range(q_count)]
    
    return unique_facts, fact_sequence, occurrence_map, queries_by_fact


def fact_to_question(fact):
    """Convert a fact to a question."""
    fact_lower = fact.lower()
    
    # Owner facts
    if "name is" in fact_lower:
        return "What is my owner name?"
    if "favorite food is" in fact_lower:
        return "What is my owner's favorite food?"
    if "works as" in fact_lower:
        return "What does my owner do for work?"
    if "birthday is" in fact_lower:
        return "When is my owner's birthday?"
    if "lives in" in fact_lower:
        return "Where does my owner live?"
    if "favorite color is" in fact_lower:
        return "What is my owner's favorite color?"
    if "has a cat named" in fact_lower:
        return "What is my owner's pet's name?"
    if "loves reading" in fact_lower:
        return "What does my owner like to read?"
    if "drives a" in fact_lower:
        return "What car does my owner drive?"
    if "plays guitar" in fact_lower:
        return "What does my owner do on weekends?"
    if "favorite season is" in fact_lower:
        return "What is my owner's favorite season?"
    if "speaks three languages" in fact_lower:
        return "How many languages does my owner speak?"
    if "favorite holiday is" in fact_lower:
        return "What is my owner's favorite holiday?"
    if "adopted me from" in fact_lower:
        return "Where did my owner adopt me from?"
    if "allergic to" in fact_lower:
        return "What is my owner allergic to?"
    
    # Trivia/Scientific facts
    if "sky is blue" in fact_lower:
        return "What color is the sky?"
    if "water freezes" in fact_lower:
        return "At what temperature does water freeze?"
    if "cats have four legs" in fact_lower:
        return "How many legs do cats have?"
    if "sun is a star" in fact_lower:
        return "What is the sun?"
    if "dogs are mammals" in fact_lower:
        return "What are dogs?"
    if "moon orbits" in fact_lower:
        return "What does the moon orbit?"
    if "birds can fly" in fact_lower:
        return "Can birds fly?"
    if "fish live in water" in fact_lower:
        return "Where do fish live?"
    if "earth orbits the sun" in fact_lower:
        return "What does the Earth orbit?"
    if "rain comes from clouds" in fact_lower:
        return "Where does rain come from?"
    
    # Random/Dog facts
    if "chasing butterflies" in fact_lower:
        return "What do I love chasing?"
    if "favorite toy is a squeaky ball" in fact_lower:
        return "What is my favorite toy?"
    if "sleep on a soft dog bed" in fact_lower:
        return "Where do I sleep?"
    if "fur is golden and white" in fact_lower:
        return "What color is my fur?"
    if "enjoy walks in the park" in fact_lower:
        return "Where do I enjoy walks?"
    
    return f"What about: {fact[:30]}?"


def run_test(verbose=False):
    unique_facts, fact_sequence, occurrence_map, queries_by_fact = generate_test_data()
    
    print("="*70)
    print("Frequency-Based Memory Test")
    print("="*70)
    print(f"Total unique facts: {len(unique_facts)}")
    print(f"Total fact occurrences: {len(fact_sequence)}")
    print(f"Total queries: {sum(len(q) for q in queries_by_fact.values())}")
    print("Memory capacity: 10 items")
    print()
    
    # Count words
    avg_fact_words = sum(len(f.split()) for f in unique_facts) / len(unique_facts)
    print(f"Average words per fact: {avg_fact_words:.1f}")
    print()
    
    # Build sequence - queries appear with probability decreasing over time
    import random
    random.seed(42)
    
    sequence = []
    pending_queries = {}
    
    for step, fact in enumerate(fact_sequence):
        sequence.append(("fact", fact))
        
        fact_idx = unique_facts.index(fact)
        
        if queries_by_fact[fact_idx]:
            pending_queries[fact_idx] = step
        
        if pending_queries and random.random() < 0.95:
            distances = [(abs(step - last_seen), fact_idx) for fact_idx, last_seen in pending_queries.items()]
            distances.sort()
            
            weights = [(50000 - dist) for dist, _ in distances]
            total_weight = sum(weights)
            if total_weight > 0:
                r = random.randint(0, total_weight - 1)
                
                cumulative = 0
                selected_fact_idx = None
                for (dist, f_idx), w in zip(distances, weights):
                    cumulative += w
                    if r < cumulative:
                        selected_fact_idx = f_idx
                        break
                
                if selected_fact_idx is not None:
                    del pending_queries[selected_fact_idx]
                    if queries_by_fact[selected_fact_idx]:
                        q, a = queries_by_fact[selected_fact_idx].pop(0)
                        sequence.append(("query", (q, a)))
    
    for fact_idx in range(30):
        for q, a in queries_by_fact[fact_idx]:
            sequence.append(("query", (q, a)))
    
    # Count facts and queries in sequence
    fact_count = sum(1 for t, _ in sequence if t == "fact")
    query_count = sum(1 for t, _ in sequence if t == "query")
    
    print(f"Sequence: {fact_count} facts, {query_count} queries")
    print()
    print("Running benchmark...")
    print()
    
    memory = PixelMemory(max_items=10)
    evaluator = Evaluator(memory)
    
    results, query_results = evaluator.run_benchmark(sequence, verbose=verbose)
    
    correct = sum(query_results)
    total = len(query_results)
    accuracy = correct / total if total > 0 else 0
    
    print()
    print("="*70)
    print("DETAILED RESULTS")
    print("="*70)
    print(f"Correct: {correct}/{total} ({accuracy:.1%})")
    print(f"Wrong: {total - correct}/{total}")
    print()
    
    # Track results with details
    memory2 = PixelMemory(max_items=10)
    
    query_details = []
    
    for item_type, content in sequence:
        if item_type == "fact":
            memory2.learn(content)
        else:
            question, expected = content
            result = memory2.query(question)
            
            if result is not None:
                returned_fact = result[0]
                if returned_fact == "I forgot that((":
                    matched = False
                else:
                    matched = expected.lower() in returned_fact.lower().replace("**", "")
            else:
                returned_fact = "NO MATCH"
                matched = False
            
            # Find which fact this is
            fact_idx = None
            for i, f in enumerate(unique_facts):
                if f == expected:
                    fact_idx = i
                    break
            
            query_details.append({
                "question": question,
                "expected": expected,
                "returned": returned_fact,
                "matched": matched,
                "fact_idx": fact_idx
            })
    
    print("Wrong answers (first 20):")
    print("-" * 70)
    wrong_count = 0
    for i, qd in enumerate(query_details):
        if not qd["matched"]:
            wrong_count += 1
            if wrong_count <= 20:
                print(f"{wrong_count}. Q: {qd['question'][:40]}")
                print(f"   Expected: {qd['expected'][:40]}")
                print("   Got: I forgot that((")
    
    if wrong_count > 20:
        print(f"... and {wrong_count - 20} more wrong answers")
    
    print()
    print("="*70)
    
    # Analyze by occurrence count - track which queries actually matched
    print("Accuracy by occurrence count:")
    
    # We need to track which queries matched - let's re-run with tracking
    memory2 = PixelMemory(max_items=10)
    # evaluator2 not used but kept for potential future debugging
    
    # Track results per fact index
    query_results_by_fact = {i: [] for i in range(30)}
    
    # Re-run with tracking
    for item_type, content in sequence:
        if item_type == "fact":
            memory2.learn(content)
        else:
            question, expected = content
            result = memory2.query(question)
            # Find which fact this is
            fact_idx = None
            for i, f in enumerate(unique_facts):
                if f == expected:
                    fact_idx = i
                    break
            if fact_idx is not None:
                matched = result is not None and (expected.lower() in result[0].lower().replace("**", ""))
                query_results_by_fact[fact_idx].append(matched)
    
    for occ in [2, 3, 4, 5, 6, 7]:
        fact_indices = [i for i, o in occurrence_map.items() if o == occ]
        total_q = sum(len(query_results_by_fact[idx]) for idx in fact_indices)
        correct_q = sum(sum(query_results_by_fact[idx]) for idx in fact_indices)
        if total_q > 0:
            acc = correct_q / total_q
            print(f"  {occ} occurrences ({len(fact_indices)} facts, {total_q} queries): {acc:.1%}")
        else:
            print(f"  {occ} occurrences ({len(fact_indices)} facts, {total_q} queries): N/A")
    
    # Show memory state
    print()
    print("Final Memory State:")
    state = evaluator.get_memory_state()
    
    for i, item in enumerate(state, 1):
        fact_preview = item["fact"][:45] + "..." if len(item["fact"]) > 45 else item["fact"]
        print(f"  {i}. {fact_preview}")
        print(f"     Access: {item['access_count']}, Importance: {item['importance']:.1f}")
    
    print()
    print("="*70)
    
    return accuracy


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    accuracy = run_test(verbose=args.verbose)