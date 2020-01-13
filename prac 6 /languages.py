from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    languages = [ruby, python, visual_basic]
    print("dynamic typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()