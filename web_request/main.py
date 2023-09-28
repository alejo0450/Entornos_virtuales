import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app= FastAPI()#se crea una instancia  de esta ubicación

@app.get('/')#Se crea un decorador con una ruta desde la que pueden ingresar desde la web.

def get_list():
    return [1,2,3]


@app.get('/contact', response_class= HTMLResponse)#otro decorador para acceder a otra ruta

def get_list():
    return '''
        <h1>Titulo</h1>'''


def run():
    store.get_c()

if __name__ == '__main__':
    run()