calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    string = (len(string), string.upper(), string.lower())
    count_calls()
    return string

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() == str(list_to_search[i]).lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)