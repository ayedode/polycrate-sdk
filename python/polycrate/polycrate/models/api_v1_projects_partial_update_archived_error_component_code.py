from typing import Literal

ApiV1ProjectsPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_projects_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1ProjectsPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
