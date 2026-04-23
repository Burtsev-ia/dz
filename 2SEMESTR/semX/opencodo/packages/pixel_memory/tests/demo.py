#!/usr/bin/env python3
"""Demo script for Pixel's smart memory system."""

from pixel_memory import PixelMemory, Evaluator


def main():
    qa_pairs = [
        ("What is my owner's name?", "My owner's name is Sarah"),
        ("What is my owner's favorite food?", "My favorite food is pizza"),
        ("What does my owner do for work?", "My owner works as a doctor"),
        ("When is my owner's birthday?", "My owner's birthday is March 15th"),
        ("Where does my owner live?", "My owner lives in New York City"),
        ("What is my owner's favorite color?", "My owner's favorite color is purple"),
        ("What is my owner's pet's name?", "My owner has a cat named Whiskers"),
        ("What does my owner like to read?", "My owner loves reading mystery novels"),
    ]

    facts = [
        "My owner's name is Sarah",
        "The sky is blue today",
        "My favorite food is pizza",
        "Water freezes at 0 degrees Celsius",
        "My owner works as a doctor",
        "Cats have four legs",
        "My owner's birthday is March 15th",
        "The sun is a star",
        "My owner lives in New York City",
        "Dogs are mammals",
        "My owner's favorite color is purple",
        "The moon orbits the Earth",
        "My owner has a cat named Whiskers",
        "Rain comes from clouds",
        "My owner loves reading mystery novels",
        "Birds can fly",
        "My owner's favorite season is autumn",
        "The Earth orbits the sun",
        "My owner drives a blue Honda",
        "Fish live in water",
    ]

    sequence = []
    
    # Pattern 1: 2 facts, 1 question (fact first!)
    sequence.append(("fact", facts[0]))  # name Sarah
    sequence.append(("fact", facts[1]))  # sky blue
    sequence.append(("query", qa_pairs[0]))  # What is my owner's name? ✓
    
    # Pattern 2: 3 facts, 1 question (facts first!)
    sequence.append(("fact", facts[2]))  # pizza
    sequence.append(("fact", facts[3]))  # water freezes  
    sequence.append(("fact", facts[4]))  # doctor
    sequence.append(("query", qa_pairs[1]))  # What is my favorite food? ✓
    sequence.append(("query", qa_pairs[2]))  # What does my owner do? ✓
    
    # Pattern 3: 10 facts, 1 question
    for i in range(5, 15):
        sequence.append(("fact", facts[i]))
    sequence.append(("query", qa_pairs[4]))  # Where does my owner live? ✓
    
    # Pattern 4: 5 facts, 2 questions
    for i in range(15, 20):
        sequence.append(("fact", facts[i]))
    sequence.append(("query", qa_pairs[3]))  # When is birthday? ✓
    sequence.append(("query", qa_pairs[5]))  # favorite color? ✓
    sequence.append(("query", qa_pairs[6]))  # pet name? ✓
    
    # Final query after all facts learned
    sequence.append(("query", qa_pairs[7]))  # reading ✓
    
    memory = PixelMemory(max_items=10)
    evaluator = Evaluator(memory)

    print("=== Pixel's Memory System - Mixed Input Benchmark ===\n")
    print(f"Total steps: {len(sequence)}")
    print(f"Max memory capacity: 10 items\n")

    results, query_results = evaluator.run_benchmark(sequence)

    print("\n=== Results Summary ===")
    for step, accuracy in results.items():
        print(f"Step {step}: {accuracy:.1%} accuracy")

    print("\n=== Query Results ===")
    correct = sum(query_results)
    total = len(query_results)
    print(f"Correct: {correct}/{total} ({correct/total:.1%})")
    
    print("\n=== Memory State (Final) ===")
    state = evaluator.get_memory_state()
    for i, item in enumerate(state, 1):
        print(f"{i}. {item['fact'][:50]}")
        print(f"   Access: {item['access_count']}, Importance: {item['importance']:.2f}")


if __name__ == "__main__":
    main()