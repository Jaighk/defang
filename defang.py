import re
from ioc_patterns import *

def detect_ioc_type(ioc: str) -> dict:
    for pattern in PATTERNS:
        if re.match(PATTERNS[pattern], ioc):
            return {"ioc":ioc, "ioc_type": pattern}
    return {"ioc":ioc, "ioc_type": "unknown"}

def defang(ioc: dict) -> str:
    fanged_strings = [".", ":"]
    output_str = ""

    if ioc["ioc_type"] == "url":
        ioc_proto_url = ioc["ioc"].split(":")

        if len(ioc_proto_url) != 2:
            for char in ioc["ioc"]: 
                if char in fanged_strings:
                    output_str += f"[{char}]"
                else: 
                    output_str += char
        else:
            for char in ioc_proto_url[0]:
                if char != "t" and char not in fanged_strings:
                    output_str += char
                if char == "t":
                    output_str += "x"
                if char in fanged_strings: 
                    output_str += f"[{char}]"
            output_str += "[:]"
            for char in ioc_proto_url[1]:
                if char in fanged_strings:
                    output_str += f"[{char}]"
                else:
                    output_str += char

    if ioc["ioc_type"] == "email":
        for char in ioc["ioc"]:
            if char in fanged_strings:
                output_str += f"[{char}]"
            else:
                output_str += char

    if ioc["ioc_type"] == "file hash":
        output_str = ioc["ioc"]

    return output_str

def generate_output(input: list, output_file=None):
    defanged = {"urls": [],
                "email addresses": [],
                "sender domains": [],
                "file hashes": [],
                "unknown": [],
                }

    for item in input:
        ioc = detect_ioc_type(item)
        if ioc["ioc_type"] == "unknown":
            defanged["unknown"].append(defang(ioc))
        if ioc["ioc_type"] == "url":
            defanged["urls"].append(defang(ioc))
        if ioc["ioc_type"] == "email":
            defanged["email addresses"].append(defang(ioc))
            defanged["sender domains"].append(defang({"ioc":ioc["ioc"].split("@")[1], "ioc_type":"url"}))
        if ioc["ioc_type"] == "file hash":
            defanged["file hashes"].append(defang(ioc))

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
