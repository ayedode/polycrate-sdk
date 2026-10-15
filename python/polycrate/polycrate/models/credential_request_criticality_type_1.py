from typing import Literal

CredentialRequestCriticalityType1 = Literal["", "high", "low", "medium"]

CREDENTIAL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[CredentialRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_credential_request_criticality_type_1(value: str) -> CredentialRequestCriticalityType1:
    if value in CREDENTIAL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
