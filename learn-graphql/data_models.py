from dataclasses import dataclass
from datetime import datetime
import yaml
from mako.template import Template


@dataclass
class User:
    id: str
    name: str
    email: str
    password_hash: str
    created_at: datetime


@dataclass
class List:
    id: str
    user_id: str
    name: str
    created_on: datetime
    updated_on: datetime
    is_active: bool


filename = "./data/data.csvt"
data = yaml.safe_load(Template(filename=filename).render())

lists = []
for obj in data["lists"]:
    lists.append(List(**obj))

users = []
for obj in data["users"]:
    users.append(User(**obj))


def get_user_by_email(email):
    return list(filter(lambda u: u.email == email, users))[0]


def get_user(user_id):
    return list(filter(lambda u: u.id == user_id, users))[0]


def get_lists(user):
    return list(filter(lambda l: l.user_id == user.id, lists))


def get_list(user, list_id):
    return list(filter(lambda l: l.user_id == user.id and l.list_id == list_id, lists))[
        0
    ]


def find_lists(user, name_fragment, only_active):
    def predicate(list_):
        cond = list_.user_id == user.id and list_.name.find(name_fragment) != -1
        if only_active:
            cond = cond and list_.is_active
        return cond

    return list(filter(predicate, lists))
