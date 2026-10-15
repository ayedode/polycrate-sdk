from typing import Literal

ActionRunCriticalityType3Type1 = Literal["high", "low", "medium"]

ACTION_RUN_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ActionRunCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_action_run_criticality_type_3_type_1(value: str) -> ActionRunCriticalityType3Type1:
    if value in ACTION_RUN_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
