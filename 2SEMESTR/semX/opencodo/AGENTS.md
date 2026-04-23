# AGENTS.md

## Project Type
Python monorepo (multi-package)

## Packages
- `packages/pixel_memory/` - Pixel's smart memory system with semantic understanding

## Key Commands
- `python -m venv .venv` - Create virtual environment
- `source .venv/Scripts/activate` - Activate (Windows)
- `pip install -e packages/pixel_memory` - Install Pixel Memory package

## Running the Demo
```bash
cd packages/pixel_memory
python demo.py
```

## Testing
- `pytest` - Run tests
- `ruff check .` - Lint