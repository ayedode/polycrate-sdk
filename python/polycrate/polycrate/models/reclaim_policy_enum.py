from typing import Literal

ReclaimPolicyEnum = Literal["Delete", "Recycle", "Retain"]

RECLAIM_POLICY_ENUM_VALUES: set[ReclaimPolicyEnum] = {
    "Delete",
    "Recycle",
    "Retain",
}


def check_reclaim_policy_enum(value: str) -> ReclaimPolicyEnum:
    if value in RECLAIM_POLICY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RECLAIM_POLICY_ENUM_VALUES!r}")
