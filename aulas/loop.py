heros = ['Link', 'Keima Katsukagi', 'Maeda', 'Howl']

print("Heros from the fantasy history:")
for item in heros:
    string_print = f"{item}"
    print(string_print)

fruits = ['Grape', 'Apple', 'Strawberry', 'Melon', 'Pineapple']

print("\nFruits dictionaries:")
for index, item in enumerate(fruits, start=1):
    string_print = f"{index}. {item}"
    print(string_print)

print("\nInforme oque ira guardar:")
your_dic = [input("1 item: "), input("2 item: ")]

print(f"{your_dic[0]} {your_dic[1]}")
