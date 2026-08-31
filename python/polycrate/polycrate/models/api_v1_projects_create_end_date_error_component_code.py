from typing import Literal

ApiV1ProjectsCreateEndDateErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PROJECTS_CREATE_END_DATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsCreateEndDateErrorComponentCode] = {
    "datetime",
    "invalid",
}


def check_api_v1_projects_create_end_date_error_component_code(
    value: str,
) -> ApiV1ProjectsCreateEndDateErrorComponentCode:
    if value in API_V1_PROJECTS_CREATE_END_DATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_END_DATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
