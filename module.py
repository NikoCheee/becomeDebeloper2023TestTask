def unique_character(text):
    for char in text:
        if char in '.@\'\`/,:$;-!#№%*&?)({}][|':
            text = text.replace(char, '')

    splitted = text.split()
    done = []

    for element in splitted:
        for char in element:
            count = element.count(char)
            if count == 1:
                done.append(char)
                break

    for element in done:
        final = done.count(element)
        if final == 1:
            return element
    return
