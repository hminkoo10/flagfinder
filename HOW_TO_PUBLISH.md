# How to publish

## 1) Replace placeholders
Edit these before publishing:
- `Your Name`
- `you@example.com`
- `yourname` in GitHub URLs
- package name if `pickles-flagfinder` is already taken on PyPI

## 2) Install tools
```bash
python -m pip install --upgrade build twine pytest
```

## 3) Run tests
```bash
pytest
```

## 4) Build
```bash
python -m build
```

## 5) Upload manually
```bash
python -m twine upload dist/*
```

Use:
- Username: `__token__`
- Password: your PyPI token

## 6) GitHub Actions auto-publish
This repo includes `.github/workflows/publish.yml` for Trusted Publishing.

Typical flow:
1. Push this repository to GitHub
2. Create a project on PyPI
3. In PyPI, configure Trusted Publishing for your GitHub repo/workflow
4. Push a tag like:
```bash
git tag v0.1.0
git push origin v0.1.0
```

Then GitHub Actions will publish automatically.
