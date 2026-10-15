from typing import Literal

ProjectSimpleKind = Literal["offboarding", "onboarding", "ongoing"]

PROJECT_SIMPLE_KIND_VALUES: set[ProjectSimpleKind] = {
    "offboarding",
    "onboarding",
    "ongoing",
}


def check_project_simple_kind(value: str) -> ProjectSimpleKind:
    if value in PROJECT_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_SIMPLE_KIND_VALUES!r}")
