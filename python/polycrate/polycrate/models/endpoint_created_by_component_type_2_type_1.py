from typing import Literal

EndpointCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

ENDPOINT_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[EndpointCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_endpoint_created_by_component_type_2_type_1(value: str) -> EndpointCreatedByComponentType2Type1:
    if value in ENDPOINT_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENDPOINT_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
