print('Hello, sparta')

print(10)

array = [1, 2, 3, 4, 5]

print(array[4])


def IsEven(num):
    if num % 2 == 0 and num > 2:
        print("is even")
    else:
        print("is odd")


IsEven(10)

wizards = [{'name': 'Harry Potter', 'age': 40}, {'name': 'Ron Weasley', 'age': 40}]
print(wizards)

# print 로 값 확인해보기
# wizards[0]['name']의 값은? 'Harry Potter'
# wizards[1]['name']의 값은? 'Ron Weasley'

new_wizard = {'name': 'Albus Potter', 'age': 14}
wizards.append(new_wizard)
print(wizards)

# print 로 값 확인해보기
# wizards의 값은? [{'name':'Harry Potter','age':40}, {'name':'Ron Weasley','age':40}, {'name':'Albus Potter','age':14}]
# wizards[2]['name']의 값은? 'Albus Potter'

fruits = ['사과', '감', '수박', '멜론', '자두', '포도', '복숭아', '딸기']
for fruit in fruits:
    print(fruit)

fruits = ['감', '감', '감', '감', '감', '감', '감', '감', '감', '김', '감', '감', '감', '감', '감', '감']
for fruit in fruits:
    if fruit != '감':
        print(fruit)