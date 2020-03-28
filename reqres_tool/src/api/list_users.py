from requests import request
from argparse import ArgumentParser

from reqres_tool.src.config.get_config import get_config

from reqres_tool.src.models.list_users_response import ListUsersResponse


def __get_args(args):
    p = ArgumentParser()
    p.add_argument("page", type=int)
    return p.parse_args(args)


def list_users(args):
    params = __get_args(args)
    host = get_config().get("hosts", "reqres")
    endpoint = get_config().get("endpoints", "users")
    response = request("get", f"{host}/{endpoint}", params={"page": params.page})
    return ListUsersResponse(**response.json())
