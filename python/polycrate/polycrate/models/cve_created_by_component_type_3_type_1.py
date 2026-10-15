from typing import Literal

CVECreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

CVE_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[CVECreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_cve_created_by_component_type_3_type_1(value: str) -> CVECreatedByComponentType3Type1:
    if value in CVE_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}")
