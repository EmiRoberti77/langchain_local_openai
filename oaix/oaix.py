from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import User
from routers import get, post
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(post.router)
app.include_router(get.router)
app.include_router(User.router)


if __name__ == "__main__":
    uvicorn.run("oaix:app", host="0.0.0.0", port=8001, reload=True)
