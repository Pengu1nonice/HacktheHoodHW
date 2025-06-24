# lap 3

# task 1: working with strings
food = 'pepperoni pizza'
print(food[0:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

# task 2: working with lists
number_list = [1, 7675647456, 32, -5, 0, 234]
number_list.append(67)
print(number_list)
number_list.insert(3, 1000)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)
print(number_list[:3])
print(number_list[-3:])

# task 3: working with dictionaries
books = {'David Guetta and Showtek' : 'Bad David', 'Arnold Lobel' : 'frog and Toad', 'jeff kenney' : 'diary of a wimpy kid','Suzanne Collins' : 'Hunger games'}
print(books.keys())
print(books.values())
print(books.get('Arnold Lobel'))
books.pop(list(books.keys())[2])
print(books)