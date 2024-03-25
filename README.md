# Directory-Oriented Database

## ⚠️ In initial development! ⚠️

This is just a concept I'm working on, and it's **REALLY BUGGY** at this time, so **I don't recommend** using it in real projects for now.

You can also feel free to help me make this happen by using the [Issues](/issues) or [Discussions](/discussions) pages.

Please note that I'll be reviewing your PRs too, so you can help me code it!

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