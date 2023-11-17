import uvicorn


def dev():
    uvicorn.run("la_noel.main:app", port=8080, reload=True)


def start():
    uvicorn.run("la_noel.main:app", port=8080)
