from typing import Literal

PolicyScope = Literal["system", "user"]

POLICY_SCOPE_VALUES: set[PolicyScope] = {
    "system",
    "user",
}


def check_policy_scope(value: str) -> PolicyScope:
    if value in POLICY_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_SCOPE_VALUES!r}")
