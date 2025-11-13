import re

url_pattern = r"(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
sha256_file_hash_pattern = r"[0-9a-f]{64}"
email_address_pattern = r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
ip_address_pattern = r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$"

PATTERNS = {"url": re.compile(url_pattern),
            "file hash": re.compile(sha256_file_hash_pattern),
            "email": re.compile(email_address_pattern),
            "ip address": re.compile(ip_address_pattern),
            }
