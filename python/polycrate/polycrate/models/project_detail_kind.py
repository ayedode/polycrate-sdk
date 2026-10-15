from typing import Literal

ProjectDetailKind = Literal["offboarding", "onboarding", "ongoing"]

PROJECT_DETAIL_KIND_VALUES: set[ProjectDetailKind] = {
    "offboarding",
    "onboarding",
    "ongoing",
}


def check_project_detail_kind(value: str) -> ProjectDetailKind:
    if value in PROJECT_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_KIND_VALUES!r}")
