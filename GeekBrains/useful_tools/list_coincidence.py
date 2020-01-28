list_1 = ['mango', 'pineapple', 'apple', 'orange']
list_2 = ['apple', 'banana', 'mango', 'mandarin', 'grape']

list_coincidence = [fruit for fruit in list_1 if fruit in list_2]
print(list_coincidence)