from typing import Literal

CVERequestCreatedByComponentType2Type1 = Literal["", "api", "cli", "operator"]

CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES: set[CVERequestCreatedByComponentType2Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_cve_request_created_by_component_type_2_type_1(value: str) -> CVERequestCreatedByComponentType2Type1:
    if value in CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_2_TYPE_1_VALUES!r}"
    )
