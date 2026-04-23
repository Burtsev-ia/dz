#!/usr/bin/env python3
"""Large-scale test for Pixel's memory system - 100 facts, 50 queries."""

from pixel_memory import PixelMemory, Evaluator
import random


def generate_test_data():
    random.seed(42)
    
    # 40 Owner facts - consistent "My owner..." pattern
    owner_facts = [
        ("My owner name is Sarah", "My owner name is Sarah"),
        ("My owner favorite food is pizza", "My owner favorite food is pizza"),
        ("My owner works as a doctor", "My owner works as a doctor"),
        ("My owner birthday is March 15th", "My owner birthday is March 15th"),
        ("My owner lives in New York City", "My owner lives in New York City"),
        ("My owner favorite color is purple", "My owner favorite color is purple"),
        ("My owner has a cat named Whiskers", "My owner has a cat named Whiskers"),
        ("My owner loves reading mystery novels", "My owner loves reading mystery novels"),
        ("My owner drives a blue Honda", "My owner drives a blue Honda"),
        ("My owner plays guitar on weekends", "My owner plays guitar on weekends"),
        ("My owner favorite season is autumn", "My owner favorite season is autumn"),
        ("My owner speaks three languages", "My owner speaks three languages"),
        ("My owner favorite holiday is Christmas", "My owner favorite holiday is Christmas"),
        ("My owner adopted me from a shelter", "My owner adopted me from a shelter"),
        ("My owner is allergic to peanuts", "My owner is allergic to peanuts"),
        ("My owner height is five feet six", "My owner height is five feet six"),
        ("My owner favorite movie is Inception", "My owner favorite movie is Inception"),
        ("My owner works at City Hospital", "My owner works at City Hospital"),
        ("My owner favorite song is Bohemian Rhapsody", "My owner favorite song is Bohemian Rhapsody"),
        ("My owner knows how to cook Italian food", "My owner knows how to cook Italian food"),
        ("My owner has a tattoo of a paw print", "My owner has a tattoo of a paw print"),
        ("My owner favorite ice cream is mint chocolate chip", "My owner favorite ice cream is mint chocolate chip"),
        ("My owner collects vintage postcards", "My owner collects vintage postcards"),
        ("My owner runs three miles every morning", "My owner runs three miles every morning"),
        ("My owner favorite book is 1984", "My owner favorite book is 1984"),
        ("My owner dreams of visiting Japan", "My owner dreams of visiting Japan"),
        ("My owner is afraid of spiders", "My owner is afraid of spiders"),
        ("My owner volunteers at the animal shelter", "My owner volunteers at the animal shelter"),
        ("My owner makes the best pancakes", "My owner makes the best pancakes"),
        ("My owner favorite board game is Catan", "My owner favorite board game is Catan"),
        ("My owner learned to code in Python", "My owner learned to code in Python"),
        ("My owner favorite pizza topping is pepperoni", "My owner favorite pizza topping is pepperoni"),
        ("My owner drinks coffee every morning", "My owner drinks coffee every morning"),
        ("My owner has a younger brother named Tom", "My owner has a younger brother named Tom"),
        ("My owner favorite sport is tennis", "My owner favorite sport is tennis"),
        ("My owner is an early bird", "My owner is an early bird"),
        ("My owner favorite coffee brand is Starbucks", "My owner favorite coffee brand is Starbucks"),
        ("My owner loves hiking in the mountains", "My owner loves hiking in the mountains"),
        ("My owner favorite restaurant is Olive Garden", "My owner favorite restaurant is Olive Garden"),
        ("My owner plays piano beautifully", "My owner plays piano beautifully"),
    ]
    
    # 30 Trivia facts
    trivia_facts = [
        ("The sky is blue today", "The sky is blue today"),
        ("Water freezes at zero degrees Celsius", "Water freezes at zero degrees Celsius"),
        ("Cats have four legs", "Cats have four legs"),
        ("The sun is a star", "The sun is a star"),
        ("Dogs are mammals", "Dogs are mammals"),
        ("The moon orbits the Earth", "The moon orbits the Earth"),
        ("Birds can fly", "Birds can fly"),
        ("Fish live in water", "Fish live in water"),
        ("The Earth orbits the sun", "The Earth orbits the sun"),
        ("Rain comes from clouds", "Rain comes from clouds"),
        ("The ocean is salty", "The ocean is salty"),
        ("Penguins cannot fly", "Penguins cannot fly"),
        ("Stars are distant suns", "Stars are distant suns"),
        ("The moon is made of rock", "The moon is made of rock"),
        ("Lightning is electricity", "Lightning is electricity"),
        ("Roses are red flowers", "Roses are red flowers"),
        ("Ice cream is a cold dessert", "Ice cream is a cold dessert"),
        ("Chocolate is toxic to dogs", "Chocolate is toxic to dogs"),
        ("Honey never spoils", "Honey never spoils"),
        ("The Great Wall is very long", "The Great Wall is very long"),
        ("Mount Everest is the tallest mountain", "Mount Everest is the tallest mountain"),
        ("Octopuses have three hearts", "Octopuses have three hearts"),
        ("The Roman Empire fell in 476 AD", "The Roman Empire fell in 476 AD"),
        ("Diamond is the hardest natural substance", "Diamond is the hardest natural substance"),
        ("The human brain is mostly water", "The human brain is mostly water"),
        ("Venus is the hottest planet", "Venus is the hottest planet"),
        ("The heart beats one hundred thousand times per day", "The heart beats one hundred thousand times per day"),
        ("Jupiter is the largest planet", "Jupiter is the largest planet"),
        ("Saturn has beautiful rings", "Saturn has beautiful rings"),
        ("Sharks have been on Earth for four hundred million years", "Sharks have been on Earth for four hundred million years"),
    ]
    
    # 30 Random/placeholder facts
    random_facts = [
        ("My favorite toy is a squeaky ball", "My favorite toy is a squeaky ball"),
        ("I love chasing butterflies in the garden", "I love chasing butterflies in the garden"),
        ("My collar is blue with white stripes", "My collar is blue with white stripes"),
        ("I sleep on a soft dog bed", "I sleep on a soft dog bed"),
        ("My vet says I am healthy", "My vet says I am healthy"),
        ("I enjoy walks in the park", "I enjoy walks in the park"),
        ("My favorite treat is bacon bits", "My favorite treat is bacon bits"),
        ("I was born in a puppies litter", "I was born in a puppies litter"),
        ("My fur is golden and white", "My fur is golden and white"),
        ("I know how to sit and stay", "I know how to sit and stay"),
        ("I can shake paws with my left paw", "I can shake paws with my left paw"),
        ("My tail wags when I am happy", "My tail wags when I am happy"),
        ("I bark when the doorbell rings", "I bark when the doorbell rings"),
        ("I love playing fetch with my owner", "I love playing fetch with my owner"),
        ("My water bowl is always full", "My water bowl is always full"),
        ("I have a warm blanket in my crate", "I have a warm blanket in my crate"),
        ("My favorite season is spring", "My favorite season is spring"),
        ("I enjoy car rides with my head out the window", "I enjoy car rides with my head out the window"),
        ("My owner takes me to the park every Sunday", "My owner takes me to the park every Sunday"),
        ("I am a golden retriever mix", "I am a golden retriever mix"),
        ("My fur gets groomed every month", "My fur gets groomed every month"),
        ("I have a nametag on my collar", "I have a nametag on my collar"),
        ("My favorite time of day is morning walks", "My favorite time of day is morning walks"),
        ("I wait by the door when my owner comes home", "I wait by the door when my owner comes home"),
        ("My favorite spot is under the big oak tree", "My favorite spot is under the big oak tree"),
        ("I know the word treat means food", "I know the word treat means food"),
        ("My bed is next to my owner bedroom", "My bed is next to my owner bedroom"),
        ("I love it when guests come over", "I love it when guests come over"),
        ("My favorite activity is swimming", "My favorite activity is swimming"),
        ("I am good at finding hidden toys", "I am good at finding hidden toys"),
    ]
    
    all_data = trivia_facts + random_facts + owner_facts
    random.shuffle(all_data)
    
    facts = [f for f, _ in all_data[:100]]
    
    # 50 Queries - 15 owner x 2 = 30, 15 trivia x 2 = 30
    # Using EXACT expected answers from facts
    owner_queries = [
        ("What is my owner name?", "My owner name is Sarah"),
        ("What is my owner favorite food?", "My owner favorite food is pizza"),
        ("What does my owner do for work?", "My owner works as a doctor"),
        ("When is my owner birthday?", "My owner birthday is March 15th"),
        ("Where does my owner live?", "My owner lives in New York City"),
        ("What is my owner favorite color?", "My owner favorite color is purple"),
        ("What is my owner pet name?", "My owner has a cat named Whiskers"),
        ("What does my owner like to read?", "My owner loves reading mystery novels"),
        ("What car does my owner drive?", "My owner drives a blue Honda"),
        ("What does my owner do on weekends?", "My owner plays guitar on weekends"),
        ("What is my owner favorite season?", "My owner favorite season is autumn"),
        ("How many languages does my owner speak?", "My owner speaks three languages"),
        ("What is my owner favorite holiday?", "My owner favorite holiday is Christmas"),
        ("Where did my owner adopt me from?", "My owner adopted me from a shelter"),
        ("What is my owner allergic to?", "My owner is allergic to peanuts"),
    ]
    
    trivia_queries = [
        ("What color is the sky?", "The sky is blue today"),
        ("At what temperature does water freeze?", "Water freezes at zero degrees Celsius"),
        ("How many legs do cats have?", "Cats have four legs"),
        ("What is the sun?", "The sun is a star"),
        ("What are dogs?", "Dogs are mammals"),
        ("What does the moon orbit?", "The moon orbits the Earth"),
        ("Can birds fly?", "Birds can fly"),
        ("Where do fish live?", "Fish live in water"),
        ("What does the Earth orbit?", "The Earth orbits the sun"),
        ("Where does rain come from?", "Rain comes from clouds"),
        ("What is the ocean?", "The ocean is salty"),
        ("Can penguins fly?", "Penguins cannot fly"),
        ("What are stars?", "Stars are distant suns"),
        ("What is lightning?", "Lightning is electricity"),
        ("What color are roses?", "Roses are red flowers"),
    ]
    
    # Create 50 queries: 15 owner x 2 = 30, 15 trivia x 2 = 30
    queries = []
    for i in range(2):
        for q, a in owner_queries:
            queries.append((q, a))
        for q, a in trivia_queries:
            queries.append((q, a))
    
    return facts, queries


def fact_to_question(fact):
    """Convert a fact to a question."""
    fact_lower = fact.lower()
    
    if "name is" in fact_lower:
        return "What is my owner name?"
    if "favorite food is" in fact_lower:
        return "What is my owner favorite food?"
    if "works as" in fact_lower:
        return "What does my owner do for work?"
    if "birthday is" in fact_lower:
        return "When is my owner birthday?"
    if "lives in" in fact_lower:
        return "Where does my owner live?"
    if "favorite color is" in fact_lower:
        return "What is my owner favorite color?"
    if "has a cat named" in fact_lower:
        return "What is my owner pet name?"
    if "loves reading" in fact_lower:
        return "What does my owner like to read?"
    if "drives a" in fact_lower:
        return "What car does my owner drive?"
    if "plays guitar" in fact_lower:
        return "What does my owner do on weekends?"
    if "favorite season is" in fact_lower:
        return "What is my owner favorite season?"
    if "speaks three languages" in fact_lower:
        return "How many languages does my owner speak?"
    if "favorite holiday is" in fact_lower:
        return "What is my owner favorite holiday?"
    if "adopted me from" in fact_lower:
        return "Where did my owner adopt me from?"
    if "allergic to" in fact_lower:
        return "What is my owner allergic to?"
    
    if "sky is" in fact_lower:
        return "What color is the sky?"
    if "water freezes" in fact_lower:
        return "At what temperature does water freeze?"
    if "cats have" in fact_lower:
        return "How many legs do cats have?"
    if "sun is" in fact_lower:
        return "What is the sun?"
    if "dogs are" in fact_lower:
        return "What are dogs?"
    if "moon orbits" in fact_lower:
        return "What does the moon orbit?"
    if "birds can fly" in fact_lower:
        return "Can birds fly?"
    if "fish live" in fact_lower:
        return "Where do fish live?"
    if "earth orbits" in fact_lower:
        return "What does the earth orbit?"
    if "rain comes" in fact_lower:
        return "Where does rain come from?"
    
    return f"Tell me: {fact[:30]}?"


def run_test():
    random.seed(42)
    
    all_facts = [
        "My owner name is Sarah",
        "My owner favorite food is pizza",
        "My owner works as a doctor",
        "My owner lives in New York City",
        "My owner favorite color is purple",
        "My owner has a cat named Whiskers",
        "My owner plays guitar on weekends",
        "My owner speaks three languages",
        "My owner height is five feet six",
        "My owner favorite movie is Inception",
        "My owner works at City Hospital",
        "My owner favorite ice cream is mint chocolate chip",
        "My owner runs three miles every morning",
        "My owner favorite book is 1984",
        "My owner is afraid of spiders",
        "My owner makes the best pancakes",
        "My owner favorite sport is tennis",
        "My owner loves hiking in the mountains",
        "My owner has a tattoo of a paw print",
        "My owner knows how to cook Italian food",
        "The sky is blue today",
        "Water freezes at zero degrees Celsius",
        "Cats have four legs",
        "The sun is a star",
        "Dogs are mammals",
        "The moon orbits the Earth",
        "Birds can fly",
        "Fish live in water",
        "The Earth orbits the sun",
        "Rain comes from clouds",
        "The ocean is salty",
        "Penguins cannot fly",
        "Stars are distant suns",
        "Lightning is electricity",
        "Roses are red flowers",
        "Ice cream is a cold dessert",
        "Chocolate is toxic to dogs",
        "Honey never spoils",
        "The Great Wall is very long",
        "Mount Everest is the tallest mountain",
        "Octopuses have three hearts",
        "The Roman Empire fell in 476 AD",
        "Diamond is the hardest natural substance",
        "The human brain is mostly water",
        "Venus is the hottest planet",
        "The heart beats one hundred thousand times per day",
        "Jupiter is the largest planet",
        "Saturn has beautiful rings",
        "Sharks have been on Earth for four hundred million years",
        "My favorite toy is a squeaky ball",
        "I love chasing butterflies in the garden",
        "My collar is blue with white stripes",
        "I sleep on a soft dog bed",
        "My vet says I am healthy",
        "I enjoy walks in the park",
        "My favorite treat is bacon bits",
        "I was born in a puppies litter",
        "My fur is golden and white",
        "I know how to sit and stay",
        "My tail wags when I am happy",
        "I bark when the doorbell rings",
        "I love playing fetch with my owner",
        "My water bowl is always full",
        "I have a warm blanket in my crate",
        "My favorite season is spring",
        "I enjoy car rides with my head out the window",
        "My owner takes me to the park every Sunday",
        "I am a golden retriever mix",
        "My fur gets groomed every month",
        "I have a nametag on my collar",
        "My favorite time of day is morning walks",
        "I wait by the door when my owner comes home",
        "My favorite spot is under the big oak tree",
        "I know the word treat means food",
        "My bed is next to my owner bedroom",
        "I love it when guests come over",
        "My favorite activity is swimming",
        "I am good at finding hidden toys",
    ]
    
    fact_to_q = {
        "My owner name is Sarah": "What is my owner name?",
        "My owner favorite food is pizza": "What is my owner favorite food?",
        "My owner works as a doctor": "What does my owner do for work?",
        "My owner lives in New York City": "Where does my owner live?",
        "My owner favorite color is purple": "What is my owner favorite color?",
        "My owner has a cat named Whiskers": "What is my owner pet name?",
        "My owner plays guitar on weekends": "What does my owner do on weekends?",
        "My owner speaks three languages": "How many languages does my owner speak?",
        "My owner height is five feet six": "What is my owner height?",
        "My owner favorite movie is Inception": "What is my owner favorite movie?",
        "My owner works at City Hospital": "Where does my owner work?",
        "My owner favorite ice cream is mint chocolate chip": "What ice cream does my owner like?",
        "My owner runs three miles every morning": "How far does my owner run?",
        "My owner favorite book is 1984": "What is my owner favorite book?",
        "My owner is afraid of spiders": "What is my owner afraid of?",
        "My owner makes the best pancakes": "What does my owner make?",
        "My owner favorite sport is tennis": "What is my owner favorite sport?",
        "My owner loves hiking in the mountains": "Where does my owner like to hike?",
        "My owner has a tattoo of a paw print": "What tattoo does my owner have?",
        "My owner knows how to cook Italian food": "What cuisine can my owner cook?",
        "The sky is blue today": "What color is the sky?",
        "Water freezes at zero degrees Celsius": "At what temperature does water freeze?",
        "Cats have four legs": "How many legs do cats have?",
        "The sun is a star": "What is the sun?",
        "Dogs are mammals": "What are dogs?",
        "The moon orbits the Earth": "What does the moon orbit?",
        "Birds can fly": "Can birds fly?",
        "Fish live in water": "Where do fish live?",
        "The Earth orbits the sun": "What does the earth orbit?",
        "Rain comes from clouds": "Where does rain come from?",
        "The ocean is salty": "What is the ocean?",
        "Penguins cannot fly": "Can penguins fly?",
        "Stars are distant suns": "What are stars?",
        "Lightning is electricity": "What is lightning?",
        "Roses are red flowers": "What are roses?",
        "Ice cream is a cold dessert": "What is ice cream?",
        "Chocolate is toxic to dogs": "Why is chocolate bad for dogs?",
        "Honey never spoils": "What food never spoils?",
        "The Great Wall is very long": "What is the Great Wall?",
        "Mount Everest is the tallest mountain": "What is the tallest mountain?",
        "Octopuses have three hearts": "How many hearts do octopuses have?",
        "The Roman Empire fell in 476 AD": "When did the Roman Empire fall?",
        "Diamond is the hardest natural substance": "What is the hardest natural substance?",
        "The human brain is mostly water": "What is the human brain made of?",
        "Venus is the hottest planet": "Which is the hottest planet?",
        "The heart beats one hundred thousand times per day": "How many times does the heart beat per day?",
        "Jupiter is the largest planet": "Which is the largest planet?",
        "Saturn has beautiful rings": "What planet has rings?",
        "Sharks have been on Earth for four hundred million years": "How long have sharks existed?",
        "My favorite toy is a squeaky ball": "What is my favorite toy?",
        "I love chasing butterflies in the garden": "What do I love chasing?",
        "My collar is blue with white stripes": "What color is my collar?",
        "I sleep on a soft dog bed": "Where do I sleep?",
        "My vet says I am healthy": "What does my vet say?",
        "I enjoy walks in the park": "Where do I enjoy walks?",
        "My favorite treat is bacon bits": "What is my favorite treat?",
        "I was born in a puppies litter": "Where was I born?",
        "My fur is golden and white": "What color is my fur?",
        "I know how to sit and stay": "What commands do I know?",
        "My tail wags when I am happy": "When does my tail wag?",
        "I bark when the doorbell rings": "When do I bark?",
        "I love playing fetch with my owner": "What do I love playing?",
        "My water bowl is always full": "What is always full?",
        "I have a warm blanket in my crate": "What is in my crate?",
        "My favorite season is spring": "What is my favorite season?",
        "I enjoy car rides with my head out the window": "What do I enjoy about car rides?",
        "My owner takes me to the park every Sunday": "When does my owner take me to the park?",
        "I am a golden retriever mix": "What breed am I?",
        "My fur gets groomed every month": "How often does my fur get groomed?",
        "I have a nametag on my collar": "What is on my collar?",
        "My favorite time of day is morning walks": "What is my favorite time of day?",
        "I wait by the door when my owner comes home": "Where do I wait?",
        "My favorite spot is under the big oak tree": "What is my favorite spot?",
        "I know the word treat means food": "What do I know about the word treat?",
        "My bed is next to my owner bedroom": "Where is my bed?",
        "I love it when guests come over": "When do I love it?",
        "My favorite activity is swimming": "What is my favorite activity?",
        "I am good at finding hidden toys": "What am I good at?",
    }
    
    occurrence_map = {}
    for fact in all_facts:
        occurrence_map[fact] = 1
    
    for i in range(20):
        fact = all_facts[i % len(all_facts)]
        occurrence_map[fact] += 1
    
    fact_sequence = []
    for fact, count in occurrence_map.items():
        for _ in range(count):
            fact_sequence.append(fact)
    
    random.shuffle(fact_sequence)
    
    queries_by_fact = {}
    for fact, count in occurrence_map.items():
        q = fact_to_q.get(fact, f"Tell me: {fact[:30]}")
        queries_by_fact[fact] = [(q, fact) for _ in range(count)]
    
    sequence = []
    pending_queries = {}
    
    for step, fact in enumerate(fact_sequence):
        sequence.append(("fact", fact))
        
        if fact in queries_by_fact and queries_by_fact[fact]:
            pending_queries[fact] = step
        
        if pending_queries and random.random() < 0.95:
            distances = [(abs(step - last_seen), f) for f, last_seen in pending_queries.items()]
            distances.sort()
            
            weights = [(50000 - dist) for dist, _ in distances]
            total_weight = sum(weights)
            if total_weight > 0:
                r = random.randint(0, total_weight - 1)
                
                cumulative = 0
                selected_fact = None
                for (dist, f), w in zip(distances, weights):
                    cumulative += w
                    if r < cumulative:
                        selected_fact = f
                        break
                
                if selected_fact:
                    del pending_queries[selected_fact]
                    if queries_by_fact[selected_fact]:
                        q, a = queries_by_fact[selected_fact].pop(0)
                        sequence.append(("query", (q, a)))
    
    for fact in queries_by_fact:
        for q, a in queries_by_fact[fact]:
            sequence.append(("query", (q, a)))
    
    fact_count = sum(1 for t, _ in sequence if t == "fact")
    query_count = sum(1 for t, _ in sequence if t == "query")
    
    total_occurrences = sum(occurrence_map.values())
    
    print("="*70)
    print("Pixel's Memory System - Large Scale Test")
    print("="*70)
    print(f"Total unique facts: {len(all_facts)}")
    print(f"Total fact occurrences: {total_occurrences}")
    print(f"Total queries: {query_count}")
    print(f"Memory capacity: 10 items")
    print()
    print(f"Sequence: {fact_count} facts, {query_count} queries")
    print()
    print("Running benchmark...")
    print()
    
    memory = PixelMemory(max_items=10)
    evaluator = Evaluator(memory)
    
    import sys
    verbose = len(sys.argv) > 1 and sys.argv[1] == "-v"
    results, query_results = evaluator.run_benchmark(sequence, verbose=verbose)
    
    correct = sum(query_results)
    total = len(query_results)
    accuracy = correct / total if total > 0 else 0
    
    print("="*70)
    print("RESULTS")
    print("="*70)
    print(f"Correct: {correct}/{total}")
    print(f"Accuracy: {accuracy:.1%}")
    
    print()
    print("="*70)
    
    return accuracy


if __name__ == "__main__":
    accuracy = run_test()