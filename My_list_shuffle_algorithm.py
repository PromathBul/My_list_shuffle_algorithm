from random import randint

def Create_list (num):
    nums = []
    for i in range(num + 1):
        nums.append(i)
    return nums

def Shuffle_list (nums, num, depth_shuffle):
    for i in range(depth_shuffle):
        first_index = randint(0, num)
        second_index = randint(0, num)
        temporary = nums[second_index]
        nums[second_index] = nums[first_index]
        nums[first_index] = temporary
        i += 1
    return nums

num = int(input('Введите количество элементов в списке: '))
nums = []
nums = Create_list(num)
print(f'Изначальный список:\n{nums}')
depth_shuffle = int(input('Задайте глубину перемешивания, соответветсвующую количеству единичных замен: '))
nums = Shuffle_list(nums, num, depth_shuffle)
print(f'Перемешанный список:\n{nums}')