from typing import Literal

SecretManagerRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[SecretManagerRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_secret_manager_request_criticality_type_2_type_1(value: str) -> SecretManagerRequestCriticalityType2Type1:
    if value in SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
