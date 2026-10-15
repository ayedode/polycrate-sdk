from typing import Literal

WorkspacePurposeType2Type1 = Literal["", "development", "infrastructure", "platform", "production", "qa", "staging"]

WORKSPACE_PURPOSE_TYPE_2_TYPE_1_VALUES: set[WorkspacePurposeType2Type1] = {
    "",
    "development",
    "infrastructure",
    "platform",
    "production",
    "qa",
    "staging",
}


def check_workspace_purpose_type_2_type_1(value: str) -> WorkspacePurposeType2Type1:
    if value in WORKSPACE_PURPOSE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_PURPOSE_TYPE_2_TYPE_1_VALUES!r}")
