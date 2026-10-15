from typing import Literal

ActionRunKind = Literal["generic"]

ACTION_RUN_KIND_VALUES: set[ActionRunKind] = {
    "generic",
}


def check_action_run_kind(value: str) -> ActionRunKind:
    if value in ACTION_RUN_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_KIND_VALUES!r}")
