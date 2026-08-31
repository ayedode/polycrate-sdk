from typing import Literal

ApiV1ProjectsCreateBudgetedHoursModeErrorComponentAttr = Literal["budgeted_hours_mode"]

API_V1_PROJECTS_CREATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsCreateBudgetedHoursModeErrorComponentAttr
] = {
    "budgeted_hours_mode",
}


def check_api_v1_projects_create_budgeted_hours_mode_error_component_attr(
    value: str,
) -> ApiV1ProjectsCreateBudgetedHoursModeErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
