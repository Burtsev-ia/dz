#!/usr/bin/env python3
"""Debug script to see why some tests fail."""

from pixel_memory import PixelMemory

def main():
    memory = PixelMemory(max_items=10)
    
    facts = [
        "My owner's name is Sarah",      # 0
        "My favorite food is pizza",     # 1
        "My owner works as a doctor",     # 2
        "My owner's birthday is March 15th",  # 3
        "My owner lives in New York City",    # 4
        "My owner's favorite color is purple", # 5
        "My owner has a cat named Whiskers",   # 6
        "My owner loves reading mystery novels", # 7
        "My owner drives a blue Honda",     # 8
        "My owner plays guitar on weekends", # 9
        # ... rest evicted
    ]
    
    # Learn first 10 facts
    for f in facts:
        memory.learn(f)
    
    print("Memory after learning 10 facts:")
    for i, f in enumerate(memory.get_all_facts()):
        print(f"  {i}: {f}")
    
    print("\n--- Queries ---")
    
    queries = [
        ("What is my owner's name?", "My owner's name is Sarah"),
        ("What is my owner's favorite food?", "My favorite food is pizza"),
        ("What does my owner do for work?", "My owner works as a doctor"),
    ]
    
    for q, expected in queries:
        result = memory.query(q)
        if result:
            fact, kw, score = result
            match = expected.lower() in fact.lower().replace('**', '')
            print(f"Q: {q}")
            print(f"  -> {fact}")
            print(f"  Match: {'OK' if match else 'FAIL'}")
        else:
            print(f"Q: {q} -> No match")
    
    print("\n--- Learn 15 more facts ---")
    for f in facts[10:15]:
        memory.learn(f)
        print(f"Learned: {f[:40]}")
    
    print("\nMemory after 15 facts:")
    for i, f in enumerate(memory.get_all_facts()):
        print(f"  {i}: {f}")

if __name__ == "__main__":
    main()