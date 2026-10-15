from typing import Literal

SecretManagerListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

SECRET_MANAGER_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[SecretManagerListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_secret_manager_list_effective_criticality_type_2_type_1(
    value: str,
) -> SecretManagerListEffectiveCriticalityType2Type1:
    if value in SECRET_MANAGER_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
