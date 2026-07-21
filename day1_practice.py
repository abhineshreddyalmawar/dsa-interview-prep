for i in range(5):
    print(i)


coat_check = {}
coat_check['Abhinesh'] = "Grey Nissan"
coat_check['Akshay'] = "White Honda"

print(coat_check['Abhinesh'])
print(coat_check['Akshay'])


coat_check = {}
coat_check['Abhinesh'] = "Grey Nissan"
coat_check['Abhinesh'] = "White Honda"

print(coat_check['Abhinesh'])


def has_duplicate(my_list):
    seen = {}
    for num in my_list:
        if num in seen:
            return True
        seen[num] = True
    return False

my_list = [1, 2, 3, 4, 5]
print(has_duplicate(my_list))