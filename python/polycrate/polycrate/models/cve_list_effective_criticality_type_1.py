from typing import Literal

CVEListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[CVEListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_cve_list_effective_criticality_type_1(value: str) -> CVEListEffectiveCriticalityType1:
    if value in CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
