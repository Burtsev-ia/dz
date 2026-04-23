Нейронка сделала краткую документацию, если еще короче, то нужно пускать run.py и там все будет.\
т.к память маленькая оч жеско влияет сам тест, тут оставил довольно жирные проценты,\
по факту для первых двух тестах, если спрашивать рандомно, получается порядка 30-40 процентов.\
тут работает некий TF-IDF т.к. некий sentence-transformers не получилось запустить.


# Pixel Memory System

**Pixel** is a robot dog with limited memory that learns facts from an incoming stream of information. When memory fills up, it must intelligently decide which facts to forget.

## The Problem

- Memory can only hold **10 facts** at a time
- System encounters **30+ unique facts** during operation
- Accuracy must improve or stay stable over time (not degrade)

## Key Features

### Intelligent Eviction
When memory is full, the system removes the least important fact:
- **Access frequency** - Frequently accessed facts survive longer
- **Recency bias** - Newly learned facts are temporarily protected
- **Duplicate boosting** - Repeated facts gain importance (+200)
- **Semantic grouping** - Similar facts boost each other (+10)

### Semantic Understanding
- TF-IDF with sentence-transformers fallback for similarity matching
- Keyword extraction and highlighting in responses
- Semantic rewrite rules for natural language queries

### Learning from Reinforcement
- Facts accessed multiple times become more important
- Successful recalls reinforce memory

## Installation

```bash
cd packages/pixel_memory
pip install -e .
```

## Usage

```python
from pixel_memory import PixelMemory

memory = PixelMemory(max_items=10)

# Learn facts
memory.learn("My owner name is Sarah")
memory.learn("My favorite toy is a squeaky ball")

# Query memory
result = memory.query("What is my owner name?")
# Returns: ("My **owner** **name** is Sarah", ["owner", "name"], 0.85)

result = memory.query("What is my favorite toy?")
# Returns: ("My **favorite** **toy** is a squeaky ball", ["favorite", "toy"], 0.82)
```

## Running Tests

```bash
cd packages/pixel_memory
python run.py
```

### Available Tests

1. **Frequency Test** - 30 unique facts with varied occurrences
2. **Large Test** - 78 unique facts stress test
3. **Comprehensive Test** - Multiple patterns
4. **Demo** - Simple interactive demo
5. **Custom** - Interactive custom test

### Current Results

| Test | Accuracy |
|------|----------|
| Frequency (30 facts, 10 slots) | 71.7% |
| Large (78 facts, 10 slots) | 57.1% |

## Architecture

```
pixel_memory/
├── src/pixel_memory/
│   ├── __init__.py          # Package exports
│   ├── memory.py            # Core PixelMemory class
│   ├── item.py              # MemoryItem with importance scoring
│   ├── similarity.py       # TF-IDF similarity engine
│   ├── keywords.py          # Keyword extraction & highlighting
│   └── evaluator.py        # Benchmark runner
├── tests/
│   ├── test_frequency.py   # Frequency-based test
│   ├── test_large.py       # Large scale test
│   ├── test_comprehensive.py
│   ├── demo.py
│   └── ...
└── run.py                   # Test runner
```

## How Eviction Works

When memory reaches 10 items:
1. Compute importance for all items: `base + access_count + recency_bonus + duplicate_boost`
2. Find the item with lowest importance
3. Remove that item
4. Add new fact

Importance formula:
```
importance = base_importance 
          + (access_count * 1.0) 
          + recency_bonus 
          + duplicate_boost
```

## License

MIT