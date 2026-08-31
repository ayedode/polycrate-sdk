from typing import Literal

ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponentCode = Literal["invalid_choice"]

API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_projects_update_budgeted_hours_interval_error_component_code(
    value: str,
) -> ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponentCode:
    if value in API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
