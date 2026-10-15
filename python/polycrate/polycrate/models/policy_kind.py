from typing import Literal

PolicyKind = Literal["generic"]

POLICY_KIND_VALUES: set[PolicyKind] = {
    "generic",
}


def check_policy_kind(value: str) -> PolicyKind:
    if value in POLICY_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_KIND_VALUES!r}")
