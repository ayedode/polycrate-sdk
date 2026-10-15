from typing import Literal

CVECriticalityType1 = Literal["", "high", "low", "medium"]

CVE_CRITICALITY_TYPE_1_VALUES: set[CVECriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_cve_criticality_type_1(value: str) -> CVECriticalityType1:
    if value in CVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_CRITICALITY_TYPE_1_VALUES!r}")
