from typing import Literal

SecretManagerCriticalityType1 = Literal["", "high", "low", "medium"]

SECRET_MANAGER_CRITICALITY_TYPE_1_VALUES: set[SecretManagerCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_secret_manager_criticality_type_1(value: str) -> SecretManagerCriticalityType1:
    if value in SECRET_MANAGER_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_CRITICALITY_TYPE_1_VALUES!r}")
