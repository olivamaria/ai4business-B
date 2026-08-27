#!/usr/bin/env python3
"""Verifica se os links Markdown relativos deste repo apontam para arquivos que existem de fato.

Uso:
    python3 check_links.py [caminho_raiz_do_repo]

Ignora links http(s)/mailto e âncoras puras (#secao). Não valida se a âncora
existe dentro do arquivo de destino, só se o arquivo existe.
"""
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
IGNORE_DIRS = {".git", ".claude", "node_modules"}


def strip_code(text: str) -> str:
    """Remove trechos de código (inline e blocos ```) antes de procurar links,
    já que links mostrados como exemplo dentro de crase não são navegação real."""
    lines = text.split("\n")
    out = []
    in_fence = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence:
            out.append("")
        else:
            out.append(INLINE_CODE_RE.sub("", line))
    return "\n".join(out)


def find_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if any(part in IGNORE_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def check_file(md_path: Path, root: Path):
    problems = []
    text = md_path.read_text(encoding="utf-8", errors="replace")
    cleaned = strip_code(text)
    for lineno, line in enumerate(cleaned.splitlines(), start=1):
        for match in LINK_RE.finditer(line):
            target = match.group(1).strip()

            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]

            target_path = target.split("#", 1)[0].strip()
            if not target_path:
                continue

            resolved = (md_path.parent / target_path).resolve()
            if not resolved.exists():
                problems.append((lineno, target, resolved))
    return problems


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    if not root.exists():
        print(f"Caminho não encontrado: {root}")
        sys.exit(2)

    total_broken = 0
    for md_path in sorted(find_markdown_files(root)):
        problems = check_file(md_path, root)
        if problems:
            rel = md_path.relative_to(root)
            print(f"\n{rel}")
            for lineno, target, resolved in problems:
                print(f"  linha {lineno}: link para '{target}' não resolve (esperado em {resolved})")
            total_broken += len(problems)

    print()
    if total_broken == 0:
        print("Nenhum link quebrado encontrado.")
        sys.exit(0)
    else:
        print(f"{total_broken} link(s) quebrado(s) encontrado(s).")
        sys.exit(1)


if __name__ == "__main__":
    main()
