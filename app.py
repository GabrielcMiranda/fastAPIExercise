from fastapi import FastAPI
from views import user_router, song_router
import uvicorn

app = FastAPI()

@app.get('/',tags=['Home'])
def home():
    return {
        'hello' : 'world'
    }

app.include_router(user_router)
app.include_router(song_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
