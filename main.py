from fastapi import FastAPI
from github_api.router import router

app = FastAPI()
app.include_router(router,prefix="/github")



