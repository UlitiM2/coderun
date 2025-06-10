import sys
import re


def count_uniq_words(text):
    words = re.findall(r"\S+", text)
    uniq_words = set(words)
    return len(uniq_words)


input_text = sys.stdin.read()
print(count_uniq_words(input_text))
