from typing import Literal

ActionRunScope = Literal["system", "user"]

ACTION_RUN_SCOPE_VALUES: set[ActionRunScope] = {
    "system",
    "user",
}


def check_action_run_scope(value: str) -> ActionRunScope:
    if value in ACTION_RUN_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_SCOPE_VALUES!r}")
