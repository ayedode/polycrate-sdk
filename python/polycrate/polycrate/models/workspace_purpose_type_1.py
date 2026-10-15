from typing import Literal

WorkspacePurposeType1 = Literal["", "development", "infrastructure", "platform", "production", "qa", "staging"]

WORKSPACE_PURPOSE_TYPE_1_VALUES: set[WorkspacePurposeType1] = {
    "",
    "development",
    "infrastructure",
    "platform",
    "production",
    "qa",
    "staging",
}


def check_workspace_purpose_type_1(value: str) -> WorkspacePurposeType1:
    if value in WORKSPACE_PURPOSE_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_PURPOSE_TYPE_1_VALUES!r}")
