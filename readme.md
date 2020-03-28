# ReqRes Tool!

![screenshot](https://i.imgur.com/0v3Tzd1.png)

This is a demonstration repository to show how we can leverage `@dataclass` decorators to represent HTTP response JSONs using Python classes!

Normally, we do not know what "shape" we will get back from our HTTP requests when we work with an API, and so we have to resort to things like `response.json()["data"]["blah"]["other_thing"]` et cetera.a

Leveraging the `@dataclass` feature, we can correlate response JSON data so that we can just do `response.json().data.blah.other_thing`, which is much cleaner and easier for others to maintain!

## To use

After running `pip install -r requirements.txt`, all you have to do is run `python . list_users` to see the result, as below:

## Notes

The main point of interest to observe is in the `reqres_tool/src/models` folder. These `@dataclass` classes are used in the `reqres_tool/src/api` folder. The entry point is, of course, `__main__.py`.

Thanks for checking out this demonstration repository!
