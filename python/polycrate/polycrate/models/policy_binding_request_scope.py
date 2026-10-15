from typing import Literal

PolicyBindingRequestScope = Literal["system", "user"]

POLICY_BINDING_REQUEST_SCOPE_VALUES: set[PolicyBindingRequestScope] = {
    "system",
    "user",
}


def check_policy_binding_request_scope(value: str) -> PolicyBindingRequestScope:
    if value in POLICY_BINDING_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_BINDING_REQUEST_SCOPE_VALUES!r}")
