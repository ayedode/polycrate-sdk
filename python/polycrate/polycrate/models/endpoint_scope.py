from typing import Literal

EndpointScope = Literal["system", "user"]

ENDPOINT_SCOPE_VALUES: set[EndpointScope] = {
    "system",
    "user",
}


def check_endpoint_scope(value: str) -> EndpointScope:
    if value in ENDPOINT_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_SCOPE_VALUES!r}")
