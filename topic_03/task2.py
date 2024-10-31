def functions():
   
    my_list = [5, 3, 8, 1, 2]
    print("Початковий список:", my_list)
    
    my_list.append(10)
    print("Після додавання елемента 10 за допомогою append():", my_list)
    
    my_list.extend([4, 7])
    print("Після додавання [4, 7] за допомогою extend():", my_list)
    
    my_list.insert(2, 6)
    print("Після вставки 6 на позицію 2 за допомогою insert():", my_list)
    
    my_list.remove(1)
    print("Після видалення елемента 3 за допомогою remove():", my_list)
    
    copied_list = my_list.copy()
    my_list.clear()
    print("Після очищення списку за допомогою clear():", my_list)
 
    copied_list.sort()
    print("Після сортування списку за допомогою sort():", copied_list)

    copied_list.reverse()
    print("Після зміни порядку елементів списку за допомогою reverse():", copied_list)

    new_list = copied_list.copy()
    print("Скопійований список за допомогою copy():", new_list)

functions()
