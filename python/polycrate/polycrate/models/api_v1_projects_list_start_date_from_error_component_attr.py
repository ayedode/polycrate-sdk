from typing import Literal

ApiV1ProjectsListStartDateFromErrorComponentAttr = Literal["start_date_from"]

API_V1_PROJECTS_LIST_START_DATE_FROM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsListStartDateFromErrorComponentAttr
] = {
    "start_date_from",
}


def check_api_v1_projects_list_start_date_from_error_component_attr(
    value: str,
) -> ApiV1ProjectsListStartDateFromErrorComponentAttr:
    if value in API_V1_PROJECTS_LIST_START_DATE_FROM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_START_DATE_FROM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
