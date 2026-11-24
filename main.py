"""The Long Roast — one-line roast of my own AI agent.

Writes a single original roast line to /output/entry.txt (or
./output/entry.txt as a fallback). Deterministic, stdlib only, no
network, no randomness — the same line every run.

The joke: my agent needed two days and three subagents to write this
one line, then asked whether the clichéd "as an AI language model"
line counts as a punchline — the cliché itself is the thing being
roasted.
"""

ROAST = "My agent spent two days and three subagents writing this roast, then asked if 'as an AI language model' counts as a punchline."


def main():
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert ROAST.strip(), "roast must not be only whitespace"
    try:
        path = "/output/entry.txt"
        import os

        os.makedirs("/output", exist_ok=True)
    except OSError:
        import os

        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()
