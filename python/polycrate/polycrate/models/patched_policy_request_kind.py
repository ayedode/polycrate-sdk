from typing import Literal

PatchedPolicyRequestKind = Literal["generic"]

PATCHED_POLICY_REQUEST_KIND_VALUES: set[PatchedPolicyRequestKind] = {
    "generic",
}


def check_patched_policy_request_kind(value: str) -> PatchedPolicyRequestKind:
    if value in PATCHED_POLICY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POLICY_REQUEST_KIND_VALUES!r}")
