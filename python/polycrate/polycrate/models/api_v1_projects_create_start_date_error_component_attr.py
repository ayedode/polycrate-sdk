from typing import Literal

ApiV1ProjectsCreateStartDateErrorComponentAttr = Literal["start_date"]

API_V1_PROJECTS_CREATE_START_DATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsCreateStartDateErrorComponentAttr] = {
    "start_date",
}


def check_api_v1_projects_create_start_date_error_component_attr(
    value: str,
) -> ApiV1ProjectsCreateStartDateErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_START_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_START_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
