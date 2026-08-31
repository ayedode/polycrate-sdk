from typing import Literal

ApiV1ProjectsUpdateEndDateErrorComponentCode = Literal["datetime", "invalid"]

API_V1_PROJECTS_UPDATE_END_DATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsUpdateEndDateErrorComponentCode] = {
    "datetime",
    "invalid",
}


def check_api_v1_projects_update_end_date_error_component_code(
    value: str,
) -> ApiV1ProjectsUpdateEndDateErrorComponentCode:
    if value in API_V1_PROJECTS_UPDATE_END_DATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_END_DATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
