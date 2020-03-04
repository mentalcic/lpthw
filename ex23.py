import sys

script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    print(">>>> main", repr(language_file), encoding, errors)  # debug print
    line = language_file.readline()
    if line:
        print(">> there's a line", repr(line))  # debug print
        print_line(line, encoding, errors)
        print(">> calling main again")  # debug print
        return main(language_file, encoding, errors)
    print("<<<< exit main")  # debug print


def print_line(line, encoding, errors):
    print(">> print_line", repr(line), encoding, errors)  # debug print
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
    print("<< exit print_line", )  # debug print


languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
