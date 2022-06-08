def solution_1(word):
    wordinator = str(len(word)) + "000"
    vowels = "aoieu"
    if vowels.find(word[-1]) > -1:
        wordinator = word + "-" + "inator " + wordinator
    else:
        wordinator = word + "inator " + wordinator
    print(wordinator)


def solution_2(word):
    last_char = word[-1]
    result = ''
    if last_char in ['a', 'e', 'i', 'o', 'u']:
        result = f'{word}-inator {len(word)}000'
    else:
        result = f'{word}inator {len(word)}000'
    return result


def solution_3(prefix):
    last_char = prefix[-1]
    output = ''
    if last_char == 'a' or last_char == 'e' or last_char == 'i' or last_char == 'e' or last_char == 'o' or last_char == 'u' :
        output = prefix + '-inator'
    else:
        output = prefix + 'inator'

    output = output + ' ' + str(len(prefix)) + "000"
    print(output)



word = input()

print('---- solution 1')
solution_1("Shrink")
solution_1("EvilClone")
solution_1(word)

print('---- solution 2')
print(solution_2("Shrink"))
print(solution_2("EvilClone"))
print(solution_2(word))

print('---- solution 3')
solution_3("Shrink")
solution_3("EvilClone")
solution_3(word)
