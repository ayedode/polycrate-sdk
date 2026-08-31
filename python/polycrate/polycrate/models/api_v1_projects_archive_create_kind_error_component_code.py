from typing import Literal

ApiV1ProjectsArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PROJECTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_projects_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1ProjectsArchiveCreateKindErrorComponentCode:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
