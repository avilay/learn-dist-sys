"""
Needs to have -
float
int
bytes
str
enum
datetime
bool

VideoGame
rating: float
num_reviews: int
thumbnail: bytes
title: str
genre: enum
released_on: datetime
is_on_pc: bool
"""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class Genre(Enum):
    FAMILY_KIDS = auto()
    SHOOTER = auto()
    ROLE_PLAYING = auto()


@dataclass
class VideoGame:
    rating: float
    num_reviews: int
    thumbnail_jpeg: bytes
    title: str
    genre: Genre
    released_on: datetime
    is_on_pc: bool


with open("./minecraft.jpeg", "rb") as f:
    minecraft_thumbnail = f.read()

minecraft = VideoGame(
    rating=5,
    num_reviews=2_399_600,
    thumbnail_jpeg=minecraft_thumbnail,
    title="Minecraft",
    genre=Genre.FAMILY_KIDS,
    released_on=datetime.strptime("2017-09-19", "%Y-%m-%d"),
    is_on_pc=True,
)

print(minecraft)


@dataclass
class Cookie:
    flavor: str
    calories: int
