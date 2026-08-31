from typing import Literal

ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponentAttr = Literal["budgeted_hours"]

API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponentAttr
] = {
    "budgeted_hours",
}


def check_api_v1_projects_partial_update_budgeted_hours_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateBudgetedHoursErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
