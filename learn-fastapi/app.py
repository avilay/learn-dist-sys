import asyncio
import random

from fastapi import Body, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

posts = [
    {"postId": 1, "title": "Post One", "content": "This is post one"},
    {"postId": 2, "title": "Post Two", "content": "This is post two"},
    {"postId": 3, "title": "Post Three", "content": "This is post three"},
]


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )


@app.get("/posts")
async def get_posts():
    # await asyncio.sleep(2)
    # if random.random() < 0.3:
    #     raise RuntimeError("KA-BOOM!")
    return posts


@app.post("/posts")
async def create_post(post: dict = Body(...)):
    # In a real app, you'd save to a database. Here, just echo back.
    posts.append(post)
