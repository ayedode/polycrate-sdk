from typing import Literal

PatchedWorkspaceRequestKind = Literal["generic", "polycrate"]

PATCHED_WORKSPACE_REQUEST_KIND_VALUES: set[PatchedWorkspaceRequestKind] = {
    "generic",
    "polycrate",
}


def check_patched_workspace_request_kind(value: str) -> PatchedWorkspaceRequestKind:
    if value in PATCHED_WORKSPACE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_WORKSPACE_REQUEST_KIND_VALUES!r}")
