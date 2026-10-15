from typing import Literal

EndpointRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[EndpointRequestCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_endpoint_request_created_by_component_type_3_type_1(
    value: str,
) -> EndpointRequestCreatedByComponentType3Type1:
    if value in ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENDPOINT_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
