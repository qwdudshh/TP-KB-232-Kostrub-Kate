initial_list = [5, 8, 9, 2, 4, 5, 1, 7]
print("Список:", initial_list)

sorted_list = sorted(initial_list)
print("Відсортований список:", sorted_list)

def insert_in_sorted_list(sorted_list, new_element):
    position = find_insert_position(sorted_list, new_element)
    sorted_list.insert(position, new_element)
    return sorted_list

def find_insert_position(sorted_list, new_element):
    for i, element in enumerate(sorted_list):
        if new_element <= element:
            return i
    return len(sorted_list)

new_element = 6
print("Новий елемент для вставки:", new_element)

updated_list = insert_in_sorted_list(sorted_list, new_element)
print("Список після вставки:", updated_list)
