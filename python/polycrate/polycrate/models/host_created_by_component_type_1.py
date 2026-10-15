from typing import Literal

HostCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

HOST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[HostCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_host_created_by_component_type_1(value: str) -> HostCreatedByComponentType1:
    if value in HOST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}")
