from typing import Literal

PatchedWorkspaceRequestScope = Literal["system", "user"]

PATCHED_WORKSPACE_REQUEST_SCOPE_VALUES: set[PatchedWorkspaceRequestScope] = {
    "system",
    "user",
}


def check_patched_workspace_request_scope(value: str) -> PatchedWorkspaceRequestScope:
    if value in PATCHED_WORKSPACE_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_WORKSPACE_REQUEST_SCOPE_VALUES!r}")
