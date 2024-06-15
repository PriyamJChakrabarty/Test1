from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'data':'Hello!'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=4000)