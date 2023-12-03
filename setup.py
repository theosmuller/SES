from __future__ import annotations
from pathlib import Path
import setuptools


def read_multiline_as_list(file_path: Path | str) -> list[str]:
    with open(file_path) as req_file:
        contents = req_file.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


requirements = read_multiline_as_list("requirements.txt")

setuptools.setup(
    name="ses",
    version="0.0.1",
    packages=setuptools.find_namespace_packages(exclude=["tests"]),
    python_requires=">=3.11",
    install_requires=requirements,
)