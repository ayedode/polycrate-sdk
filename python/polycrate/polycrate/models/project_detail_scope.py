from typing import Literal

ProjectDetailScope = Literal["system", "user"]

PROJECT_DETAIL_SCOPE_VALUES: set[ProjectDetailScope] = {
    "system",
    "user",
}


def check_project_detail_scope(value: str) -> ProjectDetailScope:
    if value in PROJECT_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_SCOPE_VALUES!r}")
