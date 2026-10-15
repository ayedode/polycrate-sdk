from typing import Literal

PatchedCVERequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_CVE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PatchedCVERequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_cve_request_criticality_type_3_type_1(value: str) -> PatchedCVERequestCriticalityType3Type1:
    if value in PATCHED_CVE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CVE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
