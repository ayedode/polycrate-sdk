from typing import Literal

PolicyRequestKind = Literal["generic"]

POLICY_REQUEST_KIND_VALUES: set[PolicyRequestKind] = {
    "generic",
}


def check_policy_request_kind(value: str) -> PolicyRequestKind:
    if value in POLICY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_REQUEST_KIND_VALUES!r}")
