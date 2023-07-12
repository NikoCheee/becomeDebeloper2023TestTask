def unique_character(text: str):
    if text.isspace():
        return "Не можна вводити тільки пробіли!"
    if text == '':
        return "Не можна вводити пустий текст!"

    splitted = text.split()
    done = []

    for element in splitted:
        for char in element:
            if char.isalpha():
                count = element.count(char)
                if count == 1:
                    done.append(char)
                    break

    for element in done:
        final = done.count(element)
        if final == 1:
            return element
    return 'У тексті немає унікальних літер!'
