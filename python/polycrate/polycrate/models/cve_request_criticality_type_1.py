from typing import Literal

CVERequestCriticalityType1 = Literal["", "high", "low", "medium"]

CVE_REQUEST_CRITICALITY_TYPE_1_VALUES: set[CVERequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_cve_request_criticality_type_1(value: str) -> CVERequestCriticalityType1:
    if value in CVE_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
