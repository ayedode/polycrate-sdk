from typing import Literal

PolicyBindingScope = Literal["system", "user"]

POLICY_BINDING_SCOPE_VALUES: set[PolicyBindingScope] = {
    "system",
    "user",
}


def check_policy_binding_scope(value: str) -> PolicyBindingScope:
    if value in POLICY_BINDING_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_BINDING_SCOPE_VALUES!r}")
