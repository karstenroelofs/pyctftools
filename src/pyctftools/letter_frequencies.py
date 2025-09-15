import json
from typing import Dict


ENGLISH_FREQS_UT = {
    "A": 0.082,
    "B": 0.015,
    "C": 0.028,
    "D": 0.043,
    "E": 0.127,
    "F": 0.022,
    "G": 0.020,
    "H": 0.061,
    "I": 0.07,
    "J": 0.0015,
    "K": 0.0077,
    "L": 0.040,
    "M": 0.024,
    "N": 0.067,
    "O": 0.075,
    "P": 0.019,
    "Q": 0.00095,
    "R": 0.060,
    "S": 0.063,
    "T": 0.091,
    "U": 0.028,
    "V": 0.0098,
    "W": 0.024,
    "X": 0.0015,
    "Y": 0.020,
    "Z": 0.00074,
}

ENGLISH_FREQS = {
    "E": 0.1202,
    "T": 0.0910,
    "A": 0.0812,
    "O": 0.0768,
    "I": 0.0731,
    "N": 0.0695,
    "S": 0.0628,
    "R": 0.0602,
    "H": 0.0592,
    "D": 0.0432,
    "L": 0.0398,
    "U": 0.0288,
    "C": 0.0271,
    "M": 0.0261,
    "F": 0.0230,
    "Y": 0.0211,
    "W": 0.0209,
    "G": 0.0203,
    "P": 0.0182,
    "B": 0.0149,
    "V": 0.0111,
    "K": 0.0069,
    "X": 0.0017,
    "Q": 0.0011,
    "J": 0.0010,
    "Z": 0.0070,
}

SUPPORTED_LANGUAGES = {"english": ENGLISH_FREQS, "english-ut": ENGLISH_FREQS_UT}


def from_json(file: str) -> Dict:
    with open(file, "r") as f:
        # TODO some type of checking
        dict = json.load(f)
        del dict["language"]
        return dict
