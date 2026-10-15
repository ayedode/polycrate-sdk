from typing import Literal

EndpointRequestScope = Literal["system", "user"]

ENDPOINT_REQUEST_SCOPE_VALUES: set[EndpointRequestScope] = {
    "system",
    "user",
}


def check_endpoint_request_scope(value: str) -> EndpointRequestScope:
    if value in ENDPOINT_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_REQUEST_SCOPE_VALUES!r}")
