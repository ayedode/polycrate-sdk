from typing import Literal

HostRequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[HostRequestCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_host_request_created_by_component_type_2_type_1(value: str) -> HostRequestCreatedByComponentType2Type1:
    if value in HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
