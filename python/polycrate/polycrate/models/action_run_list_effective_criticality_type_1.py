from typing import Literal

ActionRunListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ACTION_RUN_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ActionRunListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_action_run_list_effective_criticality_type_1(value: str) -> ActionRunListEffectiveCriticalityType1:
    if value in ACTION_RUN_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTION_RUN_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
