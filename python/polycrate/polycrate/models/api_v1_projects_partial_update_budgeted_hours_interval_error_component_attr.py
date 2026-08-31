from typing import Literal

ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponentAttr = Literal["budgeted_hours_interval"]

API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponentAttr
] = {
    "budgeted_hours_interval",
}


def check_api_v1_projects_partial_update_budgeted_hours_interval_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateBudgetedHoursIntervalErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
