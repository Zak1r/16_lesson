#list = [10, 20, 30, 40, 50]
# императивнқе == как сделать
# деклоративнқе == что сделать

# list = [10, 20, 30, 40, 50]
# print(min(list))
# print(list[::-1])
# list.reverse()


# list = [10, 20, 30, 40, 50]
# for i in range(len(list)-1, -1, -1):
#     print(list[i])


# new_list = []
# list = [10, 20, 30, 40, 50]
# for num in list[len(list)::-1]:
#     new_list.append(num)
# print(new_list)


# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# filtered_nums = []
# for num in nums:
#     if num <= 50:    filtered_nums.append(num)
# print(filtered_nums)

# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# filtered_nums = []
# def myFilter(list):
#     for num in list:
#         if num <= 50:    filtered_nums.append(num) 
#     return filtered_nums
# print(myFilter([10, 20, 30, 40, 50, 60, 70, 80, 90]))

# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# def myFilter(list, targetNumber):
#     for num in list:
#         filtered_nums = []
#         if num <= targetNumber:    
#             filtered_nums.append(num) 
#     return filtered_nums
# print(myFilter([10, 20, 30, 40, 50, 60, 70, 80, 90], 60))
# print(myFilter([10, 20, 30, 40, 50, 60, 70, 80, 90], 30))



# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# def myFilter(func, list, targetNumber):
#     for num in list:
#         filtered_nums = []
#         result = func(num, targetNumber)
#         if result:    
#             filtered_nums.append(num) 
#     return filtered_nums

# def less(num, target):
#     return num < target
# def greater(num, target):
#     return num > target

# print(myFilter(less, [10, 20, 30, 40, 50, 60, 70, 80, 90], 50))
# print(myFilter(greater, [10, 20, 30, 40, 50, 60, 70, 80, 90], 30))


'''напишите 4 функции для сложения, вычитания, умножения и деления
вызов функций должен выглядеть так:
calculator(add, 2, 3) -> 5
calculator(divide, 10, 2) -> 5.0
calculator(subtract, 10, 2) -> 8
calculator(multiply, 10, 2) ->20'''

# def calculator(func, a, b):
#     return func(a, b)
# def add (a, b):
#     return a + b

# def divide (a, b):
#     return a / b

# def subtract (a, b):
#     return a - b

# def multiply (a, b):
#     return a * b

# print(calculator(add, 2, 3) )
# print(calculator(divide, 10, 2) )
# print(calculator(subtract, 10, 2))
# print(calculator(multiply, 10, 2))


# def sum_numbers(txt: str):
#     acc = 0
#     list = txt.split(' ')
#     for word in list:
#         if word.isdigit():  acc += int(word)
#     return acc
# print(sum_numbers('hi'))
# print(sum_numbers('who is 1st here'))
# print(sum_numbers('my numbers is 2'))
# print(sum_numbers('this picture is an oil on canvas'))
# print(sum_numbers('Petersen between 1845 and 1910 year'))


def checkio(array):
    if len(array) == 0: return 0
    else:   
        last = array[-1]
        evens = array [::2]
        total = 0
        for i in evens:
            total = total + i
        return total * last 
           
print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([6]))
print(checkio([]))


