from typing import Literal

SecretManagerEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

SECRET_MANAGER_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[SecretManagerEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_secret_manager_effective_criticality_type_2_type_1(value: str) -> SecretManagerEffectiveCriticalityType2Type1:
    if value in SECRET_MANAGER_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
