#!/usr/bin/env python3
"""Debug script to see what's matching."""

from pixel_memory import PixelMemory

def main():
    memory = PixelMemory(max_items=10)
    
    facts_and_queries = [
        (True, "My owner's name is Sarah"),
        (True, "The sky is blue today"),
        (True, "My favorite food is pizza"),
        (True, "Water freezes at 0 degrees Celsius"),
        (True, "My owner works as a doctor"),
        (True, "My owner's birthday is March 15th"),
        (True, "My owner lives in New York City"),
        (True, "My owner's favorite color is purple"),
        (True, "My owner has a cat named Whiskers"),
        (True, "My owner loves reading mystery novels"),
    ]
    
    for is_fact, content in facts_and_queries:
        if is_fact:
            memory.learn(content)
            print(f"Learned: {content}")
    
    print(f"\nMemory has {len(memory)} facts\n")
    
    queries = [
        ("What is my owner's name?", "My owner's name is Sarah"),
        ("What is my owner's favorite food?", "My favorite food is pizza"),
        ("What does my owner do for work?", "My owner works as a doctor"),
        ("When is my owner's birthday?", "My owner's birthday is March 15th"),
        ("Where does my owner live?", "My owner lives in New York City"),
        ("What is my owner's favorite color?", "My owner's favorite color is purple"),
        ("What is my owner's pet's name?", "My owner has a cat named Whiskers"),
        ("What does my owner like to read?", "My owner loves reading mystery novels"),
    ]
    
    for q, expected in queries:
        result = memory.query(q)
        if result:
            fact, keywords, score = result
            match = expected.lower() in fact.lower().replace('**', '')
            print(f"Q: {q}")
            print(f"  Got: {fact[:60]}")
            print(f"  Keywords: {keywords}, Score: {score:.3f}")
            print(f"  Match: {'OK' if match else 'FAIL'}")
        else:
            print(f"Q: {q}")
            print(f"  No match")
        print()

if __name__ == "__main__":
    main()