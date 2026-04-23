#!/usr/bin/env python3
"""Pixel Memory Test Runner."""

import subprocess
import sys
import os
import argparse

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(PACKAGE_DIR, "src")
TESTS_DIR = os.path.join(PACKAGE_DIR, "tests")


def get_env():
    env = os.environ.copy()
    env["PYTHONPATH"] = SRC_DIR
    return env


def run_custom_test():
    sys.path.insert(0, SRC_DIR)
    from pixel_memory import PixelMemory
    
    print("\n=== Custom Test Mode ===")
    print("Enter facts (empty line to finish):")
    facts = []
    while True:
        f = input("fact> ").strip()
        if not f:
            break
        facts.append(f)
    
    print("\nEnter queries (empty line to finish):")
    queries = []
    while True:
        q = input("query> ").strip()
        if not q:
            break
        queries.append(q)
    
    if not facts or not queries:
        print("Need at least one fact and one query!")
        return
    
    memory = PixelMemory(max_items=10)
    for fact in facts:
        memory.learn(fact)
    
    print("\n" + "="*50)
    print("Running queries...")
    print("="*50 + "\n")
    
    for q in queries:
        result = memory.query(q)
        if result:
            ans = result[0]
            print(f"Q: {q}")
            print(f"A: {ans}\n")
        else:
            print(f"Q: {q}")
            print(f"A: I forgot that((\n")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Pixel Memory Test Runner")
    parser.add_argument("--test", "-t", type=int, choices=[1,2,3,4,5], 
                       help="Test number to run (1-5)")
    parser.add_argument("--list", "-l", action="store_true", 
                       help="List available tests")
    args = parser.parse_args()
    
    # Change to package directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    test_choice = args.test
    
    if args.list:
        print("Available tests:")
        print("1. Frequency     - 30 facts with varied occurrences (shows history)")
        print("2. Large         - 100+ facts test (shows history)")
        print("3. Comprehensive - Multiple test patterns (shows history)")
        print("4. Demo          - Simple demo (shows history)")
        print("5. Custom        - Interactive custom test")
        print("\nUsage: python run.py --test 1")
        return
    
    if test_choice is None:
        print("="*50)
        print("Pixel Memory Test Runner")
        print("="*50)
        print()
        print("1. Frequency test")
        print("2. Large test")
        print("3. Comprehensive test")
        print("4. Demo")
        print("5. Custom test (interactive)")
        print()
        
        choice = input("Select test (1-5): ").strip()
    else:
        choice = str(test_choice)
    
    if choice == "1":
        subprocess.run([sys.executable, os.path.join(TESTS_DIR, "test_frequency.py"), "-v"], env=get_env())
    elif choice == "2":
        subprocess.run([sys.executable, os.path.join(TESTS_DIR, "test_large.py"), "-v"], env=get_env())
    elif choice == "3":
        subprocess.run([sys.executable, os.path.join(TESTS_DIR, "test_comprehensive.py"), "-v"], env=get_env())
    elif choice == "4":
        subprocess.run([sys.executable, os.path.join(TESTS_DIR, "demo.py"), "-v"], env=get_env())
    elif choice == "5":
        run_custom_test()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()