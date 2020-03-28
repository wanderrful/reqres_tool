from argparse import ArgumentParser

from reqres_tool.src.api.list_users import list_users


def main(script, params):
    if script == "list_users":
        # Assume page 1, if not specified
        if len(params) < 1:
            params = ["1"]

        users = list_users(params)
        for user in users.data:
            # Notice how we can now reference the HTTP response JSON as though it were a named class!
            print(f"# user_id={user.id} first_name={user.first_name} last_name={user.last_name} email={user.email}")


def __get_args():
    p = ArgumentParser()
    p.add_argument("script")
    p.add_argument("params", nargs="*")
    return p.parse_args()


if __name__ == "__main__":
    args = __get_args()
    main(args.script, args.params)
