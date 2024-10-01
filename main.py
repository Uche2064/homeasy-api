from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import utilisateur
app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(utilisateur.router)