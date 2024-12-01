import re


def normalize_whitespace(text):
    return re.sub(r" +", " ", re.sub(r"[\t\r]", " ", text))


def get_numeric(text):
    return re.sub(r"[^\d.]", "", text)
