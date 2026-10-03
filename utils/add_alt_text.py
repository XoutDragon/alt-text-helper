#given an image, edit the html file to add the new alt text
from utils.bot import ImageBot

import re
from html import escape
from pathlib import Path


IMG_TAG = re.compile(r"""<img\b(?:"[^"]*"|'[^']*'|[^'">])*?>""", re.IGNORECASE)
SRC_ATTR = re.compile(r"""\bsrc\s*=\s*(["'])(.*?)\1""", re.IGNORECASE)
ALT_ATTR = re.compile(
    r"""\balt\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+)""",
    re.IGNORECASE,
)


def add_alt_text_under_images(html_file: str, alt_texts: dict[str, str]) -> None:
    path = Path(html_file)
    html = path.read_text(encoding="utf-8")

    def replace_image(match: re.Match[str]) -> str:
        image_tag = match.group()
        src_match = SRC_ATTR.search(image_tag)
        if src_match is None:
            return image_tag

        text = alt_texts.get(src_match.group(2))
        if text is None:
            return image_tag

        safe_text = escape(text, quote=True)
        if ALT_ATTR.search(image_tag):
            image_tag = ALT_ATTR.sub(f'alt="{safe_text}"', image_tag, count=1)
        else:
            image_tag = re.sub(
                r"\s*/?>$",
                lambda ending: f' alt="{safe_text}"{ending.group()}',
                image_tag,
            )

        return f'{image_tag}<p class="image-alt-text">{escape(text)}</p>'

    path.write_text(IMG_TAG.sub(replace_image, html), encoding="utf-8")