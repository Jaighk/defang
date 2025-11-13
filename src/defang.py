import re


from src.ioc import (
    Indicator,
    URL,
    IP,
    SHA256FileHash,
    Email,
    Unknown,
)
from src.ioc_patterns import *


def process_iocs(input_file: str) -> dict[str, str]:
    iocs: list[Indicator] = []
    with open(input_file, "r") as file:
        for line in file.readlines():
            iocs.append(detect_ioc_type(line))
        file.close()
    defanged: dict[str, str] = collect_defanged(iocs=iocs)
    return defanged

def detect_ioc_type(ioc: str) -> Indicator:
    for pattern in PATTERNS:
        if re.match(PATTERNS[pattern], ioc):
            if pattern == "url": 
                return URL(ioc)
            if pattern == "file hash":
                return SHA256FileHash(ioc)
            if pattern == "email":
                return Email(ioc)
            if pattern == "ip address": 
                return IP(ioc)
    return Unknown(ioc)

def collect_defanged(iocs: list[Indicator]) -> dict[str, str]:
    defanged_iocs = {}
    for ioc in iocs:
        if not str(type(ioc)) in defanged_iocs.keys():
            defanged_iocs[str(type(ioc))] = [ioc.defang()]
        else:
            defanged_iocs[str(type(ioc))].append(ioc.defang())
    return defanged_iocs


def generate_output(defanged_iocs: dict[str, str], output_file: str | None = None) -> None:
    title = "# Defanged IoCs\n"
    print(title)
    for type in defanged_iocs:
        print(f"## {type}\n")
        print("```shell")
        for ioc in defanged_iocs[type]:
            print(f"{ioc}")
        print("```")

    if output_file != None:
        print(f"Writing to file: {output_file}")
        with open(output_file, "w") as f:
            f.write(title + "\n")
            for type in defanged_iocs:
                f.write(f"## {type}\n\n")
                for ioc in defanged_iocs[type]:
                    f.write(f"{ioc}\n")
                f.write("\n")
