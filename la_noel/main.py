import random

from fastapi import FastAPI, HTTPException

from .request_model import Draw
from .utils import has_duplicate_names, inner_category, max_count, outter_category

app = FastAPI()


@app.get("/")
async def root():
    return "hello world!"


@app.post("/v1/secret-santa-draw")
async def secret_santa(draw: Draw):
    participants = draw.participants

    if has_duplicate_names(participants):
        raise HTTPException(
            status_code=422,
            detail="Their are a duplicate name in the participants list.",
        )

    givers = participants.copy()
    receivers = participants.copy()

    pair = []
    while True:
        category = max_count(givers)

        inner = inner_category(givers, category)
        outter = outter_category(receivers, category)

        giver = random.choice(inner)
        receiver = random.choice(outter if len(outter) > 0 else participants)

        givers.remove(giver)
        receivers.remove(receiver)

        pair.append({"giver": giver.name, "receiver": receiver.name})

        if len(givers) == 0:
            break

    return {"result": pair}


# if _name_ == "_main_":
#     category_field = "cat"
#     json_path = "members.json"

#     with open(json_path) as members_file:
#         members = json.load(members_file)

#     pair = secret_santa(members)

#     emoji = "🔔🎉🎅🎁🎄🧦🌟"
#     for m in pair:
#         print(f"{random.choice(emoji)} {m[0]['name'].capitalize()} est le secret santa de {m[1]['name'].capitalize()}.")
