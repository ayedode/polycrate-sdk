from typing import Literal

PolicyBindingListScope = Literal["system", "user"]

POLICY_BINDING_LIST_SCOPE_VALUES: set[PolicyBindingListScope] = {
    "system",
    "user",
}


def check_policy_binding_list_scope(value: str) -> PolicyBindingListScope:
    if value in POLICY_BINDING_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_BINDING_LIST_SCOPE_VALUES!r}")
