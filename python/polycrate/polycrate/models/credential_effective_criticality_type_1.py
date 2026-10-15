from typing import Literal

CredentialEffectiveCriticalityType1 = Literal["high", "low", "medium"]

CREDENTIAL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[CredentialEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_credential_effective_criticality_type_1(value: str) -> CredentialEffectiveCriticalityType1:
    if value in CREDENTIAL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
