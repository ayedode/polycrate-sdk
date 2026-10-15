from typing import Literal

CredentialCriticalityType1 = Literal["", "high", "low", "medium"]

CREDENTIAL_CRITICALITY_TYPE_1_VALUES: set[CredentialCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_credential_criticality_type_1(value: str) -> CredentialCriticalityType1:
    if value in CREDENTIAL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_CRITICALITY_TYPE_1_VALUES!r}")
