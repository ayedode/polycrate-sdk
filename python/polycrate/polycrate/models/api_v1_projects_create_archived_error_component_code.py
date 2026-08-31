from typing import Literal

ApiV1ProjectsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsCreateArchivedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_projects_create_archived_error_component_code(
    value: str,
) -> ApiV1ProjectsCreateArchivedErrorComponentCode:
    if value in API_V1_PROJECTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
