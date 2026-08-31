from typing import Literal

ApiV1ProjectsUpdateBudgetedHoursErrorComponentAttr = Literal["budgeted_hours"]

API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsUpdateBudgetedHoursErrorComponentAttr
] = {
    "budgeted_hours",
}


def check_api_v1_projects_update_budgeted_hours_error_component_attr(
    value: str,
) -> ApiV1ProjectsUpdateBudgetedHoursErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
