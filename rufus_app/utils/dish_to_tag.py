import difflib
import requests
import json
from ..models import Menu, Dish, DishItem

def get_closest_matches(d):
    new_d = {}
    for key, value in d.items():
        closest_match, closest_match_id = '', ''
        for k, v in d.items():
            matches = difflib.get_close_matches(key, [k], n=1, cutoff=0.8)
            if matches:
                closest_match = k
                closest_match_id = v[0][0] if v else ''
                break
        new_d[key] = {'closest_match': closest_match, 'closest_match_id': closest_match_id}
    return new_d

def get_menu_items(nombres,platos, data):
    #print('platos ',platos)
    menu_id = data['id']
    lista_tags = ['food', 'gastronomy', 'feeding', 'ultra-processed food']
    ingredients_dict = dict()

    lista_objs_dishes = []
    for nombre,plato in zip(nombres, platos):
        print(nombres)
        menu = Menu.objects.get(id=menu_id)

        # create a new Dish object and associate it with the Menu object
        dish = Dish(menu=menu)
        dish.nombre = nombre
        dish.plato = str(plato)
        
        dish.save()
        for elem in plato:
            url = f'https://api.arasaac.org/api/pictograms/es/search/{elem.replace(" ", "%20")}?offset=0&tab=0'
            
            response = requests.get(url)
            # Obtener los pictogramas si existen
            if response.ok:
                data = response.json()
                for i in data: 
                    for tag in i['tags']: 
                        if tag in lista_tags:
                            for keyword in i['keywords']:
                                ingredient = elem.lower()
                                if ingredient not in ingredients_dict:
                                    ingredients_dict[ingredient] = []
                                ingredients_dict[ingredient].append([i['_id'], keyword['keyword']])
    return ingredients_dict
