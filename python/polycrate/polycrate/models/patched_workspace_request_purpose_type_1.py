from typing import Literal

PatchedWorkspaceRequestPurposeType1 = Literal[
    "", "development", "infrastructure", "platform", "production", "qa", "staging"
]

PATCHED_WORKSPACE_REQUEST_PURPOSE_TYPE_1_VALUES: set[PatchedWorkspaceRequestPurposeType1] = {
    "",
    "development",
    "infrastructure",
    "platform",
    "production",
    "qa",
    "staging",
}


def check_patched_workspace_request_purpose_type_1(value: str) -> PatchedWorkspaceRequestPurposeType1:
    if value in PATCHED_WORKSPACE_REQUEST_PURPOSE_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_WORKSPACE_REQUEST_PURPOSE_TYPE_1_VALUES!r}")
