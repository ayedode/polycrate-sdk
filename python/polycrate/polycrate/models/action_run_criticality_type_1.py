from typing import Literal

ActionRunCriticalityType1 = Literal["high", "low", "medium"]

ACTION_RUN_CRITICALITY_TYPE_1_VALUES: set[ActionRunCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_action_run_criticality_type_1(value: str) -> ActionRunCriticalityType1:
    if value in ACTION_RUN_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_CRITICALITY_TYPE_1_VALUES!r}")
