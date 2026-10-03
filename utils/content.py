import regex as re

def get_content(
    html_filepath: str, resources_dir: str = "./resources"
) -> str:
    """Extracts h2 and p contents from an HTML file and returns them as one string."""
    with open(html_filepath, "r", encoding="utf-8") as f:
        html = f.read()

    matches = re.findall(
        r"<(h2|p)\b[^>]*>(.*?)</\1\s*>",
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )

    return "\n".join(text.strip() for _, text in matches)
