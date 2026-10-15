from typing import Literal

PatchedCVERequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_CVE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedCVERequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_cve_request_criticality_type_2_type_1(value: str) -> PatchedCVERequestCriticalityType2Type1:
    if value in PATCHED_CVE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CVE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
