from typing import Literal

ContactGroupListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

CONTACT_GROUP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ContactGroupListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_contact_group_list_effective_criticality_type_2_type_1(
    value: str,
) -> ContactGroupListEffectiveCriticalityType2Type1:
    if value in CONTACT_GROUP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
