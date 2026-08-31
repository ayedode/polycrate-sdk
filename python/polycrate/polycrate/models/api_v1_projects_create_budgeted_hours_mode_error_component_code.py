from typing import Literal

ApiV1ProjectsCreateBudgetedHoursModeErrorComponentCode = Literal["invalid_choice"]

API_V1_PROJECTS_CREATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsCreateBudgetedHoursModeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_projects_create_budgeted_hours_mode_error_component_code(
    value: str,
) -> ApiV1ProjectsCreateBudgetedHoursModeErrorComponentCode:
    if value in API_V1_PROJECTS_CREATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
