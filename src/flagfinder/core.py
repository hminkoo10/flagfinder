import re


def findflag(prefix: str, text: str):
    pattern = rf"{re.escape(prefix)}\{{[^{{}}]*\}}"
    match = re.search(pattern, text)
    return match.group(0) if match else None


def findflags(prefix: str, text: str):
    pattern = rf"{re.escape(prefix)}\{{[^{{}}]*\}}"
    return re.findall(pattern, text)


def findflag_labeled(label: str, prefix: str, text: str):
    flag = findflag(prefix, text)
    return f"{label}: {flag}" if flag else None


def findflags_labeled(label: str, prefix: str, text: str):
    flags = findflags(prefix, text)
    return [f"{label}: {flag}" for flag in flags]