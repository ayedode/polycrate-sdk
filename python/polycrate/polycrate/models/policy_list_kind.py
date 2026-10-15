from typing import Literal

PolicyListKind = Literal["generic"]

POLICY_LIST_KIND_VALUES: set[PolicyListKind] = {
    "generic",
}


def check_policy_list_kind(value: str) -> PolicyListKind:
    if value in POLICY_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_LIST_KIND_VALUES!r}")
