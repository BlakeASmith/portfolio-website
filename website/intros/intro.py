from website import parsing
from typing import Literal
from pathlib import Path
from dataclasses import dataclass

import marko
from bs4 import BeautifulSoup

CONTENT_PATH = Path(__file__).parent.parent.parent/"content"

intros_md = (CONTENT_PATH / "intros").glob("*.md")
Position = Literal["first", "second", "third"]


@dataclass
class IntroSection:
    title: str
    position: Position = "first"
    icon: str = "fa fa-microchip"
    content: str = "..."


def parse_intro_markdown(path: Path) -> IntroSection:
    text = path.read_text()
    lines = text.split("\n")
    metadata, lines = parsing.parse_yaml_metadata(lines)
    html = marko.convert("\n".join(lines))
    soup = BeautifulSoup(html)

    return IntroSection(title=metadata["title"], content=str(soup),
                        icon=metadata["icon"] if "icon" in metadata else "fa-microchip")


def parse_intros_from_content_directory():
    return [parse_intro_markdown(path) for path in intros_md]
