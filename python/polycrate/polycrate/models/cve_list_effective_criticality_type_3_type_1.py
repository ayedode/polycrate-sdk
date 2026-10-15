from typing import Literal

CVEListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[CVEListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_cve_list_effective_criticality_type_3_type_1(value: str) -> CVEListEffectiveCriticalityType3Type1:
    if value in CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
