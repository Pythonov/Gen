TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:admin@127.0.0.1:5432/gen"},
    "apps": {
        "models": {
            "models": ["src.models.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
