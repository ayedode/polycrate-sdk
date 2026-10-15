from typing import Literal

CredentialRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

CREDENTIAL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CredentialRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_credential_request_criticality_type_2_type_1(value: str) -> CredentialRequestCriticalityType2Type1:
    if value in CREDENTIAL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDENTIAL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
