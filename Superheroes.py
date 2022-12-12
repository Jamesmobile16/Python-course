import requests

def get_all_info():
    host = 'https://akabab.github.io/superhero-api/api'
    uri = '/all.json'
    url = host + uri
    response = requests.get(url)
    return response.json()

def get_superhero_intelligence(superhero_list):
    res = {}
    for superhero in superhero_list:
        all_list = get_all_info()
        success = False
        for id in all_list:
            if id['name'] == superhero:
                success = True
                res[superhero] = id['powerstats']['intelligence']
        if not success:
            print(f'Нет такого имени: {superhero}')
    if len(res) >= 1:
        return (f'Самый умный из перечисленных, найденных: {max(res.keys())} (intelligence = {max(res.values())})')
    else:
        return 'Не найдено имён'

superhero_list = ['Hulk', 'aptain America', 'Thanos']

print(get_superhero_intelligence(superhero_list))

