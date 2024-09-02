calls = 0
def count_calls():
    global calls
    calls += 1
    return count_calls


def string_info():
    string = input('Введите слово: ')
    a = (len(string), string.upper(), string.lower())
    print (a)
    count_calls()
    return a


def is_contains(string, list_to_search):
    for i in list_to_search:
        if i == string.lower():
            print('True')
    count_calls()


string_info()
is_contains('gift', ['gift', 'present'])
print(calls)