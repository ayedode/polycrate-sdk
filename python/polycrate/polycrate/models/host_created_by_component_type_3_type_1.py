from typing import Literal

HostCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

HOST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[HostCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_host_created_by_component_type_3_type_1(value: str) -> HostCreatedByComponentType3Type1:
    if value in HOST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HOST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}")
