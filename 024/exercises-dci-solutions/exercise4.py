def inator(prefix):
    last_char = prefix[-1]
    output = ''
    if last_char == 'a' or last_char == 'e' or last_char == 'i' or last_char == 'e' or last_char == 'o' or last_char == 'u' :
        output = prefix + '-inator'
    else:
        output = prefix + 'inator'

    output = output + ' ' + str(len(prefix)) + "000"
    print(output)


inator("Shrink")
inator("Doom")
inator("EvilClone")
