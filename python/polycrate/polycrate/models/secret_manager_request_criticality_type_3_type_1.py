from typing import Literal

SecretManagerRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[SecretManagerRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_secret_manager_request_criticality_type_3_type_1(value: str) -> SecretManagerRequestCriticalityType3Type1:
    if value in SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
