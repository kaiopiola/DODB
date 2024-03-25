# Directory-Oriented Database

## ⚠️ In initial development! ⚠️

This is just a concept I'm working on, and it's **REALLY BUGGY** at this time, so **I don't recommend** using it in real projects for now.

You can also feel free to help me make this happen by using the [Issues](https://github.com/kaiopiola/DODB/issues) or [Discussions](https://github.com/kaiopiola/DODB/discussions) pages.

Please note that I'll be reviewing your PRs too, so you can help me code it!

## What in the world is this?
Directory-Oriented Database (Or just DODB, anyway) is my personal database engine project.

The idea is to separate our databases in folders, not .SQL files, and store tables data separated by files, our Database Tables file (.dbt).

It works just like a JSON from now, but I'm thinking on trying other ways to get the best performance as possible with this engine, my goal is to make it really fast for big data and queries.

## Using it

You can perform POST requests to our project API to make operations in the database, to this URL:

`http://127.0.0.1:5000/database_name/table_name`

And contaning a json like this:
```json
{
    "operation": "GET",
    "filters": [
        {
            "key": "age", "operator": ">", "value": "80"
        },
        {
           "key": "age", "operator": ">", "value": "7000"
        }
    ]
}
```

There's a lot of examples in the `/test` folder, so feel free to play with it :p