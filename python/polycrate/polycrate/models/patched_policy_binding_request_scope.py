from typing import Literal

PatchedPolicyBindingRequestScope = Literal["system", "user"]

PATCHED_POLICY_BINDING_REQUEST_SCOPE_VALUES: set[PatchedPolicyBindingRequestScope] = {
    "system",
    "user",
}


def check_patched_policy_binding_request_scope(value: str) -> PatchedPolicyBindingRequestScope:
    if value in PATCHED_POLICY_BINDING_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POLICY_BINDING_REQUEST_SCOPE_VALUES!r}")
