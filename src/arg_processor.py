import argparse
from argparse import Namespace

def process_args(args: list[str]) -> Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="defang",
        description="a simple IOC defanging tool"
        )
    
    _ = parser.add_argument(
        "-i",
        "--input-file",
        type=str,
        required=True,
        help="input file with IOCs to defang; expects a plaintext"
    )

    _ = parser.add_argument(
        "-o",
        "--output-file",
        type=str,
        required=False,
        help="output file path for defanged IOCs; outputs markdown"
    )

    return parser.parse_args()
