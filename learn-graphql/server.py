"""
To run this script:

```
uvicorn server:app
```

"""

from ariadne import (
    MutationType,
    QueryType,
    convert_kwargs_to_snake_case,
    load_schema_from_path,
    make_executable_schema,
    resolve_to,
    snake_case_fallback_resolvers,
)
from ariadne.asgi import GraphQL
from ariadne.objects import ObjectType
from dotenv import load_dotenv

import auth
import data_models as dm

query = QueryType()
mutation = MutationType()
list_ = ObjectType("List")
user = ObjectType("User")


def extract_token(info):
    auth_header = info.context["request"].headers.get("authorization", None)
    if auth_header and auth_header.startswith("Bearer"):
        return auth_header.removeprefix("Bearer").strip()
    else:
        return None


@query.field("debugUsers")
def resolve_dbg_users(_, info):
    return dm.users


@query.field("debugLists")
def resolve_dbg_lists(_, info):
    return dm.lists


@mutation.field("login")
@convert_kwargs_to_snake_case
def resolve_login(_, info, username, password):
    user = dm.get_user_by_email(username)
    if auth.authenticate_creds(user, password):
        # Note the use of snake case even though the graphql is defined in camel case
        return {
            "is_logged_in": True,
            "token": auth.generate_jwt(user),
        }
    else:
        return {"is_logged_in": False, "error_message": "Invalid credentials!"}


@query.field("allLists")
@convert_kwargs_to_snake_case
def resolve_all_lists(_, info):
    token = extract_token(info)
    user = auth.authenticate_token(token)
    return dm.get_lists(user)


@query.field("activeLists")
@convert_kwargs_to_snake_case
def resolve_active_lists(_, info, name_fragment=""):
    token = extract_token(info)
    user = auth.authenticate_token(token)
    return dm.find_lists(user, name_fragment, True)


@query.field("list")
def resolve_list(_, info, id):
    token = extract_token(info)
    user = auth.authenticate_token(token)
    return dm.get_list(user, id)


resolve_to("id")(dm.List, None)
resolve_to("userId")(dm.List, None)
resolve_to("name")(dm.List, None)
resolve_to("isActive")(dm.List, None)

resolve_to("id")(dm.User, None)
resolve_to("name")(dm.User, None)
resolve_to("email")(dm.User, None)


@user.field("createdAt")
def resolve_created_at(user, _):
    return str(user.created_at)


@list_.field("createdOn")
def resolve_created_on(list_, _):
    return str(list_.created_on)


@list_.field("updatedOn")
def resolve_updated_on(list_, _):
    return str(list_.updated_on)


def start():
    load_dotenv()
    typedefs = load_schema_from_path("./listy.graphql")
    schema = make_executable_schema(
        typedefs, query, mutation, list_, snake_case_fallback_resolvers
    )
    return GraphQL(schema, debug=True)


app = start()
