from typing import Literal

PatchedCVERequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

PATCHED_CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[PatchedCVERequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_cve_request_created_by_component_type_1(value: str) -> PatchedCVERequestCreatedByComponentType1:
    if value in PATCHED_CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CVE_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}"
    )
