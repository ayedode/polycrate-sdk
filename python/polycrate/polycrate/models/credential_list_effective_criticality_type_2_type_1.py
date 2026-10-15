from typing import Literal

CredentialListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

CREDENTIAL_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CredentialListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_credential_list_effective_criticality_type_2_type_1(
    value: str,
) -> CredentialListEffectiveCriticalityType2Type1:
    if value in CREDENTIAL_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDENTIAL_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
