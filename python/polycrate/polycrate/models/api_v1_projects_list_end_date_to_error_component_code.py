from typing import Literal

ApiV1ProjectsListEndDateToErrorComponentCode = Literal["invalid"]

API_V1_PROJECTS_LIST_END_DATE_TO_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProjectsListEndDateToErrorComponentCode] = {
    "invalid",
}


def check_api_v1_projects_list_end_date_to_error_component_code(
    value: str,
) -> ApiV1ProjectsListEndDateToErrorComponentCode:
    if value in API_V1_PROJECTS_LIST_END_DATE_TO_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_END_DATE_TO_ERROR_COMPONENT_CODE_VALUES!r}"
    )
