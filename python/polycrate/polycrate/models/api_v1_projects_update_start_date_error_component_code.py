from typing import Literal

ApiV1ProjectsUpdateStartDateErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PROJECTS_UPDATE_START_DATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsUpdateStartDateErrorComponentCode] = {
    "datetime",
    "invalid",
}


def check_api_v1_projects_update_start_date_error_component_code(
    value: str,
) -> ApiV1ProjectsUpdateStartDateErrorComponentCode:
    if value in API_V1_PROJECTS_UPDATE_START_DATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_START_DATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
