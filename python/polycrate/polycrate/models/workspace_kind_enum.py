from typing import Literal

WorkspaceKindEnum = Literal["generic", "polycrate"]

WORKSPACE_KIND_ENUM_VALUES: set[WorkspaceKindEnum] = {
    "generic",
    "polycrate",
}


def check_workspace_kind_enum(value: str) -> WorkspaceKindEnum:
    if value in WORKSPACE_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_KIND_ENUM_VALUES!r}")
