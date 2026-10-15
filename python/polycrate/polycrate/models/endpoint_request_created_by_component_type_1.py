from typing import Literal

EndpointRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[EndpointRequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_endpoint_request_created_by_component_type_1(value: str) -> EndpointRequestCreatedByComponentType1:
    if value in ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
