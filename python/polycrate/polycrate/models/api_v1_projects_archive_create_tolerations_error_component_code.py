from typing import Literal

ApiV1ProjectsArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_projects_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1ProjectsArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
