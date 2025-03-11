import re
from ioc_patterns import *
from ioc import *

def detect_ioc_type(ioc: str):
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

def build_defanged(input: list) -> dict:
    defanged = {"urls": [],
                "email addresses": [],
                "sender domains": [],
                "file hashes": [],
                "ip addresses": [],
                "unknown": [],
                }

    for item in input:
        ioc = detect_ioc_type(item)
        if isinstance(ioc, Unknown):
            defanged["unknown"].append(ioc.defang())
        if isinstance(ioc, URL):
            defanged["urls"].append(ioc.defang())
        if isinstance(ioc, IP):
            defanged["ip addresses"].append(ioc.defang())
        if isinstance(ioc, Email):
            sender_domain = ioc.value.split("@")[1]
            sender_domain = URL(sender_domain)
            defanged["email addresses"].append(ioc.defang())
            defanged["sender domains"].append(sender_domain.defang())
        if isinstance(ioc, SHA256FileHash):
            defanged["file hashes"].append(ioc.defang())

    return defanged

def generate_output(input: list, output_file=None):

    defanged = build_defanged(input)

    title = "# Defanged IoCs\n"
    print(title)
    for type in defanged:
        print(f"## {type}\n")
        print("```")
        for ioc in defanged[type]:
            print(f"{ioc}")
        print("```")

    if output_file != None:
        print(f"Writing to file: {output_file}")
        with open(output_file, "w") as f:
            f.write(title + "\n")
            for type in defanged:
                f.write(f"## {type}\n\n")
                for ioc in defanged[type]:
                    f.write(f"{ioc}\n")
                f.write("\n")
