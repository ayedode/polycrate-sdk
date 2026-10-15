from typing import Literal

ConditionInstanceDetailRequestKind = Literal["generic"]

CONDITION_INSTANCE_DETAIL_REQUEST_KIND_VALUES: set[ConditionInstanceDetailRequestKind] = {
    "generic",
}


def check_condition_instance_detail_request_kind(value: str) -> ConditionInstanceDetailRequestKind:
    if value in CONDITION_INSTANCE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_REQUEST_KIND_VALUES!r}")
