from ctypes import GetLastError
from idlelib.iomenu import encoding
import natasha.syntax
from natasha import NamesExtractor, MorphVocab

import SpaCy
import Utils


def GetFirstNames(text: str) -> str:
    print("[Natasha]: Инициализация Natasha..")
    morph_vocab = MorphVocab()
    extractor = NamesExtractor(morph_vocab)

    print("[Natasha]: Обработка текста, ождиайте..")
    processed_first_names = ""
    #last_names = []
    for match in extractor(text):
        if not match: continue
        if match.fact.first:
            processed_first_names += match.fact.first + "\n"
    print("[Natasha]: Успешно")
    return processed_first_names


def GetLastNames(text: str) -> str:
    print("[Natasha]: Инициализация Natasha..")
    morph_vocab = MorphVocab()
    extractor = NamesExtractor(morph_vocab)

    print(f"[Natasha]: Обработка текста, ождиайте..")
    processed_last_names = ""
    for match in extractor(text):
        if not match: return None
        if match.fact.last:
            processed_last_names += match.fact.last + "\n"

    return processed_last_names

def GetFirstAndLastNames(black_list: list[str]) -> list[str]:
    print("[Natasha]: Инициализация Natasha..")
    morph_vocab = MorphVocab()
    extractor = NamesExtractor(morph_vocab)

    print("[Natasha]: Обработка текста, ождиайте..")
    white_list = []
    for black in black_list:
        for match in extractor(black):
            if match.fact.last and match.fact.first:
                white_list.append(match.fact.last + " " + match.fact.first)
            elif match.fact.first:
                white_list.append(match.fact.first)
    return white_list
