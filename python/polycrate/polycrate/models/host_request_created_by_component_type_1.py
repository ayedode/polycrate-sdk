from typing import Literal

HostRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[HostRequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_host_request_created_by_component_type_1(value: str) -> HostRequestCreatedByComponentType1:
    if value in HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}")
