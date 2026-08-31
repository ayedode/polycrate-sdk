from typing import Literal

ApiV1ProjectsListStartDateToErrorComponentAttr = Literal["start_date_to"]

API_V1_PROJECTS_LIST_START_DATE_TO_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsListStartDateToErrorComponentAttr] = {
    "start_date_to",
}


def check_api_v1_projects_list_start_date_to_error_component_attr(
    value: str,
) -> ApiV1ProjectsListStartDateToErrorComponentAttr:
    if value in API_V1_PROJECTS_LIST_START_DATE_TO_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_START_DATE_TO_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
