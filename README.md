# flagfinder

A tiny Python package for finding CTF-style flags in strings.

## Install

```bash
pip install flagfinder
```

## Usage

```python
from flagfinder import findflag, findflags, findflag_labeled

text = "hello DH{test123} and DH{abc}"

print(findflag("DH", text))
# DH{test123}

print(findflags("DH", text))
# ['DH{test123}', 'DH{abc}']

print(findflag_labeled("flag", "DH", text))
# flag: DH{test123}
```