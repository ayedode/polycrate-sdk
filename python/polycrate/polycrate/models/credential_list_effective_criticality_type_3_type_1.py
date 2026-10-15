from typing import Literal

CredentialListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

CREDENTIAL_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[CredentialListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_credential_list_effective_criticality_type_3_type_1(
    value: str,
) -> CredentialListEffectiveCriticalityType3Type1:
    if value in CREDENTIAL_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDENTIAL_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
