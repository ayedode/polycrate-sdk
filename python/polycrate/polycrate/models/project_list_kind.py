from typing import Literal

ProjectListKind = Literal["offboarding", "onboarding", "ongoing"]

PROJECT_LIST_KIND_VALUES: set[ProjectListKind] = {
    "offboarding",
    "onboarding",
    "ongoing",
}


def check_project_list_kind(value: str) -> ProjectListKind:
    if value in PROJECT_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_LIST_KIND_VALUES!r}")
