from typing import Literal

CVERequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[CVERequestCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_cve_request_created_by_component_type_3_type_1(value: str) -> CVERequestCreatedByComponentType3Type1:
    if value in CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
