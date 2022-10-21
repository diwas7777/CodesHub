import hashlib
import argparse

parser = argparse.ArgumentParser(description="MD5 Cracker")
parser.add_argument("-md5", dest="hash", help="md5 hash", required = True)
parser.add_argument("-w", fest="wordlist", help="wordlist",required=True)
parsed_args = parser.parse_args()

def main():
    hash_cracked = ""
    with open(parsed_args.wordlist) as file:
        for line in file:
            line = line.strip()
            if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest() == parsed_args.hash:
                hash_cracked = line
                print("\nMD5-hash has been successfully cracked. The value is %s"%line)
        if hash_cracked == "":
            print("\n Failed to crack the hash. Try using a different dictionary")

if __name__ == "__main__":
    main()
