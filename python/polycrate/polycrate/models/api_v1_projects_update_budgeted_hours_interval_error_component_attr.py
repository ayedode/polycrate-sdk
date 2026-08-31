from typing import Literal

ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponentAttr = Literal["budgeted_hours_interval"]

API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponentAttr
] = {
    "budgeted_hours_interval",
}


def check_api_v1_projects_update_budgeted_hours_interval_error_component_attr(
    value: str,
) -> ApiV1ProjectsUpdateBudgetedHoursIntervalErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
