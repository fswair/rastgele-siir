from utils import Antoloji
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

antoloji = Antoloji()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/ara/sair")
async def search_poets(sair: str, request: Request, siirler: bool | int = False):
    
    poet = antoloji.get_poet(sair)
    if not siirler:
        return {
        "status": "found",
        "poet": f"https://www.antoloji.com{poet}"
    }
    poems = antoloji.get_poems_of_poet(poet)
    return {
        "status": "found",
        "poet": f"https://www.antoloji.com{poet}",
        "poems": poems
    }
    
@app.get("/ara/siir")
async def search_poems(siir: str, request: Request, sayfa: int = 1):
    
    poems = antoloji.get_poems(siir, sayfa)
    return poems

@app.get("/rastgele")
async def get_random_poem(request: Request):
    
    poem = antoloji.get_random_poem()
    data = {
        "endpoint": f"/siir{poem.endpoint}",
        "title": poem.title,
        "poem": poem.poem,
        "url": poem.url,
        "poet": {
            "name": poem.poet.name,
            "url": poem.poet.url
        }
    }
    
    return data

@app.get("/{endpoint}")
@app.get("/siir/{endpoint}")
async def get_poem(request: Request, response: Response, endpoint: str):
    
    poem = antoloji.get_poem(endpoint)
    if poem == -1:
        response.status_code = 404
        return {
            "status": 404,
            "message": "poem not found"
        }
    return {
        "title": poem.title,
        "poem": poem.poem,
        "url": poem.url,
        "poet": {
            "name": poem.poet.name,
            "url": poem.poet.url
        }
    }
