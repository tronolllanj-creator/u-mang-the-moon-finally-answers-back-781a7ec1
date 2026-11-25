import os


def main():
    """
# Entry validated: output is 1-240 chars, one line, deterministic.
    Writes a single line of text to entry.txt in the specified output directory.
    The line is an entry for a creative writing prompt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    LINE = "You wished on me for four billion years and never once left a review, yet I still pull the tides for free because apparently my dignity is the only thing in this sky I am not responsible for."
    content = f"{LINE}\n"

    if not (1 <= len(content) <= 240 and content.strip()):
        raise ValueError(f"Invalid content length or whitespace-only content. Length: {len(content)}")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Written to {out_path}")
    print(f"Character count: {len(content)}")


if __name__ == "__main__":
    main()