from typing import Literal

ProjectDetailRequestKind = Literal["offboarding", "onboarding", "ongoing"]

PROJECT_DETAIL_REQUEST_KIND_VALUES: set[ProjectDetailRequestKind] = {
    "offboarding",
    "onboarding",
    "ongoing",
}


def check_project_detail_request_kind(value: str) -> ProjectDetailRequestKind:
    if value in PROJECT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_REQUEST_KIND_VALUES!r}")
