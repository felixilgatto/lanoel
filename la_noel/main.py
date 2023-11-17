import random

from fastapi import FastAPI, HTTPException

from .request_model import Draw
from .utils import inner_category, max_count, outter_category

app = FastAPI()


@app.get("/")
async def root():
    return "hello world!"


@app.post("/secret-santa/draw")
async def secret_santa(draw: Draw):
    pair = []
    members = draw.members

    santas = members.copy()
    childs = members.copy()

    while True:
        category = max_count(santas)

        inner = inner_category(santas, category)
        outter = outter_category(childs, category)

        santa = random.choice(inner)
        child = random.choice(outter if len(outter) > 0 else members)

        santas.remove(santa)
        childs.remove(child)

        pair.append((santa, child))

        if len(santas) == 0:
            break

    return pair


# if _name_ == "_main_":
#     category_field = "cat"
#     json_path = "members.json"

#     with open(json_path) as members_file:
#         members = json.load(members_file)

#     pair = secret_santa(members)

#     emoji = "🔔🎉🎅🎁🎄🧦🌟"
#     for m in pair:
#         print(f"{random.choice(emoji)} {m[0]['name'].capitalize()} est le secret santa de {m[1]['name'].capitalize()}.")
