from typing import Literal

ConditionInstanceDetailKind = Literal["generic"]

CONDITION_INSTANCE_DETAIL_KIND_VALUES: set[ConditionInstanceDetailKind] = {
    "generic",
}


def check_condition_instance_detail_kind(value: str) -> ConditionInstanceDetailKind:
    if value in CONDITION_INSTANCE_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_KIND_VALUES!r}")
