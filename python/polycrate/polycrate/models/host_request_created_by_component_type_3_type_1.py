from typing import Literal

HostRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[HostRequestCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_host_request_created_by_component_type_3_type_1(value: str) -> HostRequestCreatedByComponentType3Type1:
    if value in HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
