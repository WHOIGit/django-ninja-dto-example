# Data Transfer Objects with Django Ninja

Data Transfer Objects (DTOs) is an object-oriented design pattern for encapsulating data in a layer that handles input / output concerns such as serialization and validation.

In [Django Ninja](https://django-ninja.dev/), DTOs can be implemented as [pydantic](https://docs.pydantic.dev/latest/) models, which Ninja uses via type hinting to perform automatic serialization, deserialization, and validation. A service layer then enables these DTOs to be read from and written to the backend.

The example exposes a CRUD API for a simple model called `Widget`, showing how DTOs, services, and views can be composed.

Example request bodies are provided:

* `create-widget.json` - POST to `/api/widget` with this request body to create your first widget
* `update-widget.json` - PUT to `/api/widget/{id}` with this request body to update a widget
* `bad-create-widget.json` - POST to `/api/widget` with this request body to receive a validation error

### Example validation error output

Here's the validation error detail you'll receive when POSTing `bad-create-widget.json` to `/api/widget`:

```json
{
    "detail": [
        {
            "type": "missing",
            "loc": [
                "body",
                "input",
                "name"
            ],
            "msg": "Field required"
        },
        {
            "type": "string_type",
            "loc": [
                "body",
                "input",
                "description"
            ],
            "msg": "Input should be a valid string"
        }
    ]
}
```
## Using the client

1. Install requirements:
   ```
   pip install -r client-requirements.txt
   ```
1. Acquire an authentication token using Django admin.
1. Copy `dotenv.template` to `.env` and replace the example token with your real token
1. Run the client:
   ```
   python client.py
   ```

The client exercises all endpoints and shows status codes and outputs for each one.