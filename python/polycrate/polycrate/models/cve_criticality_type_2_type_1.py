from typing import Literal

CVECriticalityType2Type1 = Literal["", "high", "low", "medium"]

CVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CVECriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_cve_criticality_type_2_type_1(value: str) -> CVECriticalityType2Type1:
    if value in CVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
