from dataclasses import dataclass
from typing import Literal, Iterable, Tuple
from pathlib import Path
from itertools import takewhile, dropwhile

import marko
import yaml
from bs4 import BeautifulSoup

Position = Literal["first", "second", "third"]

@dataclass
class IntroSection:
    title: str
    position: Position = "first"
    icon: str = "fa fa-microchip"
    content: str = "..."

def parse_yaml_metadata(lines: Iterable) -> Tuple[dict, Iterable[str]]:
    if "---" not in (line.strip() for line in lines):
        return {}

    metadata_lines_start = dropwhile(lambda x: x == "---", lines)
    metadata_lines = takewhile(lambda x: x != "---", metadata_lines_start)
    metadata = yaml.load("\n".join(metadata_lines), Loader=yaml.FullLoader)

    metadata_removed = list(metadata_lines_start)

    return metadata, metadata_removed

def parse_intro_markdown(path: Path) -> IntroSection:
    text = path.read_text()
    lines = text.split("\n")
    metadata, lines = parse_yaml_metadata(lines)
    html = marko.convert("\n".join(lines))
    soup = BeautifulSoup(html)

    return IntroSection(title=metadata["title"], content=soup,
            icon=metadata["icon"] if "icon" in metadata else "fa-microchip")
    

CONTENT_PATH = Path("content")

intros_md = (CONTENT_PATH/"intros").glob("*.md")
intros = [parse_intro_markdown(path) for path in intros_md]


index_config = dict(
        title="Blake Smith",
        section_names=["Home", "Placeholder1", "Placeholder2"],
        intro=intros,
        logo="Blake Anthony Smith",
)

print(index_config["intro"])


