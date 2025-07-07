import spacy

def GetNamesWithFileOutput(black_list: list[str]) -> list[str]:
    print("[SpaCy]: Инициализация SpaCy..")
    nlp = spacy.load("ru_core_news_sm")

    print(f"[SpaCy]: Обработка текста, ождиайте..")
    processed_names = []
    for black in black_list:
        doc = nlp(black)
        for ent in doc.ents:
            if ent.label_ == "PER":  # PER — персона (имя)
                processed_names.append(ent.text)

    print(f"[SpaCy]: Успешно")
    return processed_names
