#!/usr/bin/env python3
"""Generate a text file showing the order of facts and queries."""

import random


def generate_test_data():
    random.seed(42)
    
    # 30 Unique facts - mix of owner, trivia, and random
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
    
    occurrence_map = {
        0: 2, 1: 2, 2: 2, 3: 2, 4: 2,
        5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3,
        12: 4, 13: 4, 14: 4, 15: 4, 16: 4,
        17: 5, 18: 5, 19: 5, 20: 5, 21: 5,
        22: 6, 23: 6, 24: 6, 25: 6, 26: 6,
        27: 7, 28: 7, 29: 7,
    }
    
    fact_sequence = []
    for fact_idx, occurrences in occurrence_map.items():
        for _ in range(occurrences):
            fact_sequence.append(unique_facts[fact_idx])
    
    random.shuffle(fact_sequence)
    
    query_count_map = occurrence_map.copy()
    
    queries_by_fact = {}
    for fact_idx in range(30):
        q_count = query_count_map[fact_idx]
        fact = unique_facts[fact_idx]
        q = fact_to_question(fact)
        queries_by_fact[fact_idx] = [(q, fact) for _ in range(q_count)]
    
    return unique_facts, fact_sequence, occurrence_map, queries_by_fact


def fact_to_question(fact):
    fact_lower = fact.lower()
    
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


def generate_sequence_file():
    unique_facts, fact_sequence, occurrence_map, queries_by_fact = generate_test_data()
    
    # Build sequence with strategic query placement
    sequence = []
    occurrence_tracker = {i: 0 for i in range(30)}
    first_appearance = {}
    queries_placed = {i: 0 for i in range(30)}
    
    delayed_queries = []
    
    for fact in fact_sequence:
        sequence.append(("fact", fact))
        
        fact_idx = unique_facts.index(fact)
        occurrence_tracker[fact_idx] += 1
        
        if fact_idx not in first_appearance:
            first_appearance[fact_idx] = len(sequence) - 1
        
        total_occurrences = occurrence_map[fact_idx]
        query_positions = [1]
        if total_occurrences >= 3:
            query_positions.append(total_occurrences // 2)
        if total_occurrences >= 2:
            query_positions.append(total_occurrences)
        
        if occurrence_tracker[fact_idx] in query_positions:
            if queries_placed[fact_idx] < len(queries_by_fact[fact_idx]):
                q, a = queries_by_fact[fact_idx][queries_placed[fact_idx]]
                
                if queries_placed[fact_idx] == 0:
                    sequence.append(("query", (q, a)))
                else:
                    delayed_queries.append((q, a))
                
                queries_placed[fact_idx] += 1
    
    random.shuffle(delayed_queries)
    insert_positions = random.sample(range(len(sequence) // 2, len(sequence) - 10), len(delayed_queries))
    insert_positions.sort(reverse=True)
    
    for pos, query in zip(insert_positions, delayed_queries):
        sequence.insert(pos, ("query", query))
    
    for fact_idx in range(30):
        remaining = queries_by_fact[fact_idx][queries_placed[fact_idx]:]
        for q, a in remaining:
            sequence.append(("query", (q, a)))
    
    # Write to file
    with open("test_sequence.txt", "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("FACT AND QUERY SEQUENCE (In order of execution)\n")
        f.write("=" * 70 + "\n\n")
        
        f.write(f"Total facts: {len(fact_sequence)}\n")
        f.write(f"Total queries: {sum(len(q) for q in queries_by_fact.values())}\n")
        f.write("Memory capacity: 10 items\n\n")
        
        f.write("FACT BREAKDOWN:\n")
        f.write("  - Owner facts: 15\n")
        f.write("  - Trivia facts: 10\n")
        f.write("  - Random/Dog facts: 5\n\n")
        
        f.write("QUERY PLACEMENT:\n")
        f.write("  - First query for each fact: right after fact (early)\n")
        f.write("  - Subsequent queries: delayed, appear later in sequence\n\n")
        
        f.write("-" * 70 + "\n")
        f.write("SEQUENCE:\n")
        f.write("-" * 70 + "\n\n")
        
        step = 1
        for item_type, content in sequence:
            if item_type == "fact":
                fact_short = content[:50] + "..." if len(content) > 50 else content
                f.write(f"{step:3}. FACT   : {fact_short}\n")
            else:
                question, answer = content
                f.write(f"{step:3}. QUERY  : {question}\n")
                f.write(f"       ANSWER: {answer}\n")
            step += 1
    
    print("File written: test_sequence.txt")


if __name__ == "__main__":
    generate_sequence_file()