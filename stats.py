

def get_book_text(path):
    text = ""
    with open(path) as f:
        text = f.read()

    return text


def count_words(text):
    word_list = text.split()

    return len(word_list)


def count_letters(text):

    letter_dict = {}

    for char in text:
        if not char.isalpha():
            continue

        elif char.lower() in letter_dict:
            letter_dict[char.lower()] += 1

        else:
            letter_dict[char.lower()] = 1

    return letter_dict


def sort_on(items):

    return items["num"]


def refactor_dict(dict):
    dict_list = []
    for entry in dict:
        dict_list.append({"char": entry, "num": dict[entry]})

    return dict_list


def print_report(total_words, letter_dict, path):

    letter_list = refactor_dict(letter_dict)

    letter_list.sort(reverse=True, key=sort_on)

    print(
        f"============ BOOKBOT ============ \n Analyzing book found at {path} ")

    print(
        f"----------- Word Count ---------- \n Found {total_words} total words")

    print("--------- Character Count -------")

    for entry in letter_list:
        print(f"{entry["char"]}: {entry["num"]} \n")

    print("============= END ===============")
