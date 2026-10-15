from typing import Literal

ContactListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

CONTACT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ContactListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_contact_list_effective_criticality_type_3_type_1(value: str) -> ContactListEffectiveCriticalityType3Type1:
    if value in CONTACT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
