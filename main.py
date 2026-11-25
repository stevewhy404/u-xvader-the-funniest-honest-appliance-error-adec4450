"""The Funniest Honest Appliance Error.

Writes one honest-but-funny household-appliance error message to
/output/entry.txt. Gate: UTF-8, 1-200 characters, one line.
"""

import os

ENTRY = "Error 0xTOAST: the toaster burned your bread, blamed the bread, and has filed a warranty claim against you."


def verify(text: str) -> None:
    assert text, "entry must not be empty"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    text.encode("utf-8")


def main() -> None:
    verify(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
