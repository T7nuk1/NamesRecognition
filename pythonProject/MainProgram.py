import Natasha
import SpaCy
import Utils
import DeepSeekAPI


if __name__ == "__main__":
    with open("./black2.txt", "r", encoding="utf-8") as black_file:
        black_text = black_file.read()
    with open("./results/first_last_names_after_Natasha.txt", "w", encoding="utf-8") as Natasha_file:
        black_list = black_text.split("\n")
        Natasha_white_list = Natasha.GetFirstAndLastNames(black_list)
        Natasha_file.writelines("\n".join(Natasha_white_list))
    with open("./results/firs_last_names_after_SpaCy.txt", "w", encoding="utf-8") as SpaCy_file:
        SpaCy_white_list = SpaCy.GetNamesWithFileOutput(Natasha_white_list)
        SpaCy_file.writelines("\n".join(SpaCy_white_list))
    with open("./results/white_list_no_dup1.txt", "w", encoding="utf-8") as white_file:
        white_string = " ".join(SpaCy_white_list)
        white_words = white_string.split()
        white_list_no_dup = Utils.RemoveDuplicates(white_words)
        white_file.writelines("\n".join( white_list_no_dup))

    print(f"[MainProgram] Успешно")