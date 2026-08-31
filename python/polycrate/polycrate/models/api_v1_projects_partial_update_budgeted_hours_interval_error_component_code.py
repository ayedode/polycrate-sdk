from typing import Literal

ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponentCode = Literal["invalid_choice"]

API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_projects_partial_update_budgeted_hours_interval_error_component_code(
    value: str,
) -> ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponentCode:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
