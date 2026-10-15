from typing import Literal

CVEEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

CVE_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CVEEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_cve_effective_criticality_type_2_type_1(value: str) -> CVEEffectiveCriticalityType2Type1:
    if value in CVE_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CVE_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
