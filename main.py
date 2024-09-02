# def sort_list(list):

#     lenght = len(list)

#     for i in range(lenght):

#         for j in range(lenght):

#             if list[i.value] > list[j.value + 1]:
#                 list[i], list[j + 1] = list[j + 1], list[i]
#     return list


# list_names = [

#     {"nombre": "Luis", "edad": 34},
#     {"nombre": "Ana", "edad": 29},
#     {"nombre": "Mario", "edad": 40},
#     {"nombre": "Ana", "edad": 22},
#     {"nombre": "Luis", "edad": 25},
#     {"nombre": "Beatriz", "edad": 30},
# ]

# print(sort_list(list_names))


def contar_fs(word):
    return word.count('F')

def contar_car(word, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count += 1
    return count


print(contar_car('FffffffffFC', 'f'))
print(contar_car('FffffffffFC', 'c'))
print(contar_car('FffffffffFC', 'F'))