def main():
    text = input("Input: ")
    print(convert(text))


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()