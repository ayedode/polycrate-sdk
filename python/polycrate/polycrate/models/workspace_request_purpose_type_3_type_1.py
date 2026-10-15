from typing import Literal

WorkspaceRequestPurposeType3Type1 = Literal[
    "", "development", "infrastructure", "platform", "production", "qa", "staging"
]

WORKSPACE_REQUEST_PURPOSE_TYPE_3_TYPE_1_VALUES: set[WorkspaceRequestPurposeType3Type1] = {
    "",
    "development",
    "infrastructure",
    "platform",
    "production",
    "qa",
    "staging",
}


def check_workspace_request_purpose_type_3_type_1(value: str) -> WorkspaceRequestPurposeType3Type1:
    if value in WORKSPACE_REQUEST_PURPOSE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_REQUEST_PURPOSE_TYPE_3_TYPE_1_VALUES!r}")
