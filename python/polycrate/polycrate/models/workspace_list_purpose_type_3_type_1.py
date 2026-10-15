from typing import Literal

WorkspaceListPurposeType3Type1 = Literal["development", "infrastructure", "platform", "production", "qa", "staging"]

WORKSPACE_LIST_PURPOSE_TYPE_3_TYPE_1_VALUES: set[WorkspaceListPurposeType3Type1] = {
    "development",
    "infrastructure",
    "platform",
    "production",
    "qa",
    "staging",
}


def check_workspace_list_purpose_type_3_type_1(value: str) -> WorkspaceListPurposeType3Type1:
    if value in WORKSPACE_LIST_PURPOSE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_LIST_PURPOSE_TYPE_3_TYPE_1_VALUES!r}")
