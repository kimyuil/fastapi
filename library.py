import uvicorn
from fastapi import FastAPI
from router.Books import *

app = FastAPI()
app.include_router(routerBooks)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)