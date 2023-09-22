import requests

api_url_categories = 'https://api.escuelajs.co/api/v1/categories'

def get_c():
    r = requests.get(api_url_categories)
    print(r.status_code)
    print(r.text)
    categories= r.json()
    print(type(categories))
    for i in categories:
        print(i['name'])

       