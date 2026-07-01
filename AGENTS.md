# AGENTS.md — Python Learning Journey

Personal Python learning repo (French content). Not a production project.

## Layout

| Path | What |
|------|------|
| `hello-world/` | Single `hello.py` script |
| `learn/` | Structured learning path (phases 01–05), phases 3–5 are **empty stubs** |
| `notebooks/` | Jupyter notebooks (PCAP cert prep, OOP exploration) |
| `resources/` | `github.txt` — GitHub remote info |

## Key facts

- **No package manager config** (`pyproject.toml`, `requirements.txt`, etc. absent)
- **No tests, no CI, no lint/format config**
- **No `.git`** at this level (different from other dirs in the workspace)
- **Python 3.11** (local machine)
- Remote: `https://github.com/tawounfouet/python-learning-journey.git`
- Content language: **French** (comments, commit messages, docs)

## Learning material conventions

- `learn/01-basics/` → `02-tools/` → `03-best-practices/` → `04-frameworks/` → `05-advanced/`
- Only 01 and 02 contain actual `.md` files; 03–05 are placeholder dirs
- `learn/README.md` is the comprehensive curriculum guide with progression paths
- Tools recommended: Python 3.9+, VS Code, Ruff, Black, MyPy, pytest, Poetry/uv

## Notebooks

- `PCAP_Python Associate.ipynb` — PCAP certification preparation (Python Institute)
- `poo-exploration.ipynb` — OOP exploration in French
- Run with: `jupyter notebook` or VS Code notebook editor

## Commands

```powershell
python --version        # 3.11.0
python hello-world\hello.py
```
