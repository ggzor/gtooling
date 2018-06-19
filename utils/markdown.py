from pathlib import Path
from typing import List

def parse(s: str) -> str:
    return parse_lines(s.splitlines(keepends=True))

def parse_file(file: Path) -> str:
    with open(file) as file:
        return parse_lines(file.readlines())

def parse_lines(lines: List[str]) -> str:
    to_remove = [('`', ''), ('*', '')]

    for i in range(len(lines)):
        if lines[i].startswith('# '):
            lines[i] = lines[i][2:]
        elif lines[i].startswith('## '):
            lines[i] = '- ' + lines[i][3:-1] + ':\n'
        elif lines[i].startswith('* '):
            lines[i] = '   - ' + lines[i][2:]
        elif lines[i].startswith('> '):
            lines[i] = (' ' * 6) + lines[i][2:]
        else:
            lines[i] = (' ' * 3) + lines[i]

        for search, replacement in to_remove:
            lines[i] = lines[i].replace(search, replacement)

    return "".join(lines)
