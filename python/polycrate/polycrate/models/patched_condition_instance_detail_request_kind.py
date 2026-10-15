from typing import Literal

PatchedConditionInstanceDetailRequestKind = Literal["generic"]

PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_KIND_VALUES: set[PatchedConditionInstanceDetailRequestKind] = {
    "generic",
}


def check_patched_condition_instance_detail_request_kind(value: str) -> PatchedConditionInstanceDetailRequestKind:
    if value in PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CONDITION_INSTANCE_DETAIL_REQUEST_KIND_VALUES!r}"
    )
