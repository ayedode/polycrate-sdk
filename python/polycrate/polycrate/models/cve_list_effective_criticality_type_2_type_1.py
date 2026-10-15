from typing import Literal

CVEListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CVEListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_cve_list_effective_criticality_type_2_type_1(value: str) -> CVEListEffectiveCriticalityType2Type1:
    if value in CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CVE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
