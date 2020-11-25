from itertools import dropwhile, takewhile
from typing import Iterable, Tuple

import yaml


def parse_yaml_metadata(lines: Iterable) -> Tuple[dict, Iterable[str]]:
    if "---" not in (line.strip() for line in lines):
        return {}, ()

    metadata_lines_start = dropwhile(lambda x: x == "---", lines)
    metadata_lines = takewhile(lambda x: x != "---", metadata_lines_start)
    metadata = yaml.load("\n".join(metadata_lines), Loader=yaml.FullLoader)

    metadata_removed = list(metadata_lines_start)

    return metadata, metadata_removed

