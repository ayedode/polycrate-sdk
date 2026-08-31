from typing import Literal

ApiV1ProjectsCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsCreateActiveErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_projects_create_active_error_component_code(value: str) -> ApiV1ProjectsCreateActiveErrorComponentCode:
    if value in API_V1_PROJECTS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
