from pprint import pprint

def get_cook_book():
    with open('cook_book.txt', 'rt', encoding='utf-8') as file:
        cook_book_new = {}
        for line in file:
            dish = line.strip()
            ingridients_count = int(file.readline())
            recipe = []
            for a in range(ingridients_count):
                ingridients = file.readline().strip()
                ingredient_name, quantity, measure = ingridients.split(' | ')
                recipe.append({
                    'ingredient_name' : ingredient_name,
                    'quantity' : int(quantity),
                    'measure' : measure

                })
            file.readline()
            cook_book_new[dish] = recipe
        return cook_book_new


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    result = {}
    for dish, recipe in cook_book.items():
        if dish not in dishes:
            pass
        else:
            for ingridient in recipe:
                a = {}
                result[ingridient['ingredient_name']] = a
                a['measure'] = ingridient['measure']
                a['quantity'] = ingridient['quantity'] * person_count

    return result


# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 2))

files_list = ['1.txt', '2.txt', '3.txt']


def files_merging(files_list):
    a = {}
    for file in files_list:
        with open(file, 'rt', encoding='utf-8') as f:
            res = f.readlines()
            a[file] = len(res)
    s = dict(sorted(a.items(), key=lambda item: item[1]))
    for key, value in s.items():
        with open(key, 'rt', encoding='utf-8') as f2:
            result = f2.readlines()
        with open('merged_text.txt', 'a', encoding='utf-8') as f3:
            f3.write(f'{key}\n{value}\n{" ".join(result)}\n')


#files_merging(files_list)


