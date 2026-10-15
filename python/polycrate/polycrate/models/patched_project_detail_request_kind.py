from typing import Literal

PatchedProjectDetailRequestKind = Literal["offboarding", "onboarding", "ongoing"]

PATCHED_PROJECT_DETAIL_REQUEST_KIND_VALUES: set[PatchedProjectDetailRequestKind] = {
    "offboarding",
    "onboarding",
    "ongoing",
}


def check_patched_project_detail_request_kind(value: str) -> PatchedProjectDetailRequestKind:
    if value in PATCHED_PROJECT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PROJECT_DETAIL_REQUEST_KIND_VALUES!r}")
