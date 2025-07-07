def RemoveDuplicates(word_list: list[str]) -> list[str]:
    print(f"[Utils]: Удаление дубликатов.., длина файла - {len(word_list)}")

    unique_words = list(dict.fromkeys(word_list))

    print("[Utils]: Успешно")
    return unique_words

def LFprocessing(text) -> list[str]:
    output_text = "\n".join(text)
    return output_text

if __name__ == "__main__":
    with open("./results/white_list_no_dup1.txt", "r", encoding="utf-8") as input_file:
        input_list = input_file.read()
        no_dup = RemoveDuplicates(input_list.split())
    with open("./results/white_list_no_dup1.txt", "w", encoding="utf-8") as output_file:
        output_file.writelines("\n".join(no_dup))

