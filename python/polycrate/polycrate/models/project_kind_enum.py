from typing import Literal

ProjectKindEnum = Literal["offboarding", "onboarding", "ongoing"]

PROJECT_KIND_ENUM_VALUES: set[ProjectKindEnum] = {
    "offboarding",
    "onboarding",
    "ongoing",
}


def check_project_kind_enum(value: str) -> ProjectKindEnum:
    if value in PROJECT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_KIND_ENUM_VALUES!r}")
