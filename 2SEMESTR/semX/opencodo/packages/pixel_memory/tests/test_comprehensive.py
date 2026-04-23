#!/usr/bin/env python3
"""Comprehensive test for Pixel's memory system."""

from pixel_memory import PixelMemory, Evaluator


def create_test_data():
    facts = [
        "My owner's name is Sarah",
        "My favorite food is pizza",
        "My owner works as a doctor",
        "My owner's birthday is March 15th",
        "My owner lives in New York City",
        "My owner's favorite color is purple",
        "My owner has a cat named Whiskers",
        "My owner loves reading mystery novels",
        "My owner drives a blue Honda",
        "My owner plays guitar on weekends",
        "My owner's favorite season is autumn",
        "My owner speaks three languages",
        "My owner's favorite holiday is Christmas",
        "My owner adopted me from a shelter",
        "My owner is allergic to peanuts",
        "The sky is blue today",
        "Water freezes at 0 degrees Celsius",
        "Cats have four legs",
        "The sun is a star",
        "Dogs are mammals",
        "The moon orbits the Earth",
        "Birds can fly",
        "Fish live in water",
        "The Earth orbits the sun",
        "Rain comes from clouds",
    ]

    qa_pairs = [
        ("What is my owner's name?", "My owner's name is Sarah"),
        ("What is my owner's favorite food?", "My favorite food is pizza"),
        ("What does my owner do for work?", "My owner works as a doctor"),
        ("When is my owner's birthday?", "My owner's birthday is March 15th"),
        ("Where does my owner live?", "My owner lives in New York City"),
        ("What is my owner's favorite color?", "My owner's favorite color is purple"),
        ("What is my owner's pet's name?", "My owner has a cat named Whiskers"),
        ("What does my owner like to read?", "My owner loves reading mystery novels"),
        ("What car does my owner drive?", "My owner drives a blue Honda"),
        ("What does my owner do on weekends?", "My owner plays guitar on weekends"),
        ("What is my owner's favorite season?", "My owner's favorite season is autumn"),
        ("How many languages does my owner speak?", "My owner speaks three languages"),
        ("What is my owner's favorite holiday?", "My owner's favorite holiday is Christmas"),
        ("Where did my owner adopt me from?", "My owner adopted me from a shelter"),
        ("What is my owner allergic to?", "My owner is allergic to peanuts"),
    ]

    return facts, qa_pairs


def run_test_pattern(name, sequence, expected_correct, verbose=False):
    memory = PixelMemory(max_items=10)
    evaluator = Evaluator(memory)
    
    print(f"\n{'='*50}")
    print(f"Test: {name}")
    print(f"{'='*50}")
    
    results, query_results = evaluator.run_benchmark(sequence, verbose=verbose)
    
    correct = sum(query_results)
    total = len(query_results)
    accuracy = correct / total if total > 0 else 0
    
    print(f"\nResults: {correct}/{total} ({accuracy:.1%})")
    print(f"Expected: {expected_correct}/{total} ({expected_correct/total:.1%})")
    
    passed = correct >= expected_correct
    print(f"Status: {'PASS' if passed else 'FAIL'}")
    
    return passed, accuracy


def test_pattern_1_facts_then_queries(facts, qa_pairs, verbose=False):
    sequence = []
    
    for fact in facts[:10]:
        sequence.append(("fact", fact))
    
    for q, a in qa_pairs:
        sequence.append(("query", (q, a)))
    
    return run_test_pattern("10 facts then 15 queries", sequence, 8, verbose)


def test_pattern_2_interleaved(facts, qa_pairs, verbose=False):
    sequence = []
    
    for i in range(8):
        sequence.append(("fact", facts[i]))
        if i < 5:
            sequence.append(("query", (qa_pairs[i][0], qa_pairs[i][1])))
    
    for q, a in qa_pairs[5:]:
        sequence.append(("query", (q, a)))
    
    return run_test_pattern("Interleaved (facts first)", sequence, 7, verbose)


def test_pattern_3_queries_first(facts, qa_pairs, verbose=False):
    sequence = []
    
    sequence.append(("fact", facts[0]))
    sequence.append(("query", (qa_pairs[0][0], qa_pairs[0][1])))
    
    sequence.append(("fact", facts[1]))
    sequence.append(("query", (qa_pairs[1][0], qa_pairs[1][1])))
    
    for fact in facts[2:12]:
        sequence.append(("fact", fact))
    
    for i in range(2, 10):
        sequence.append(("query", (qa_pairs[i][0], qa_pairs[i][1])))
    
    return run_test_pattern("Mixed with early queries", sequence, 6, verbose)


def test_pattern_4_all_facts_then_queries(facts, qa_pairs, verbose=False):
    sequence = []
    
    owner_facts = [facts[i] for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
    trivia_facts = [facts[i] for i in [15,16,17,18,19,20,21,22,23,24]]
    
    for fact in trivia_facts:
        sequence.append(("fact", fact))
    
    for fact in owner_facts:
        sequence.append(("fact", fact))
    
    for q, a in qa_pairs:
        sequence.append(("query", (q, a)))
    
    return run_test_pattern("All 25 facts then 15 queries (owner last)", sequence, 10, verbose)


def test_pattern_5_random_sample(facts, qa_pairs, verbose=False):
    sequence = []
    
    for i in [15, 16, 17]:
        sequence.append(("fact", facts[i]))
    
    for i in [0, 2, 4, 6, 8, 10, 12, 14]:
        sequence.append(("fact", facts[i]))
    
    for i in range(5):
        sequence.append(("query", (qa_pairs[i][0], qa_pairs[i][1])))
    
    return run_test_pattern("Random sample (facts then queries)", sequence, 1, verbose)


def main(verbose=False):
    facts, qa_pairs = create_test_data()
    
    print("="*60)
    print("Pixel's Memory System - Comprehensive Test Suite")
    print("="*60)
    print(f"\nTotal facts available: {len(facts)}")
    print(f"Total Q&A pairs: {len(qa_pairs)}")
    print(f"Memory capacity: 10 items")
    
    results = []
    
    results.append(test_pattern_1_facts_then_queries(facts, qa_pairs, verbose))
    results.append(test_pattern_2_interleaved(facts, qa_pairs, verbose))
    results.append(test_pattern_3_queries_first(facts, qa_pairs, verbose))
    results.append(test_pattern_4_all_facts_then_queries(facts, qa_pairs, verbose))
    results.append(test_pattern_5_random_sample(facts, qa_pairs, verbose))
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    passed = sum(1 for p, _ in results if p)
    total = len(results)
    
    print(f"Tests passed: {passed}/{total}")
    
    avg_accuracy = sum(a for _, a in results) / total
    print(f"Average accuracy: {avg_accuracy:.1%}")
    
    if passed == total:
        print("\nAll tests PASSED!")
    else:
        print(f"\n{total - passed} test(s) FAILED")


if __name__ == "__main__":
    import sys
    verbose = len(sys.argv) > 1 and sys.argv[1] == "-v"
    main(verbose=verbose)