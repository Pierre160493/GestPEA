from fastapi import FastAPI

app = FastAPI(__name__)

@app.get("/")
async def root():
    return {"message": "Hello World test ici"}

if __name__ == "__main__":
    app.run()