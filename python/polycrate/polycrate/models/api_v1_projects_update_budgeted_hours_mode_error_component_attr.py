from typing import Literal

ApiV1ProjectsUpdateBudgetedHoursModeErrorComponentAttr = Literal["budgeted_hours_mode"]

API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsUpdateBudgetedHoursModeErrorComponentAttr
] = {
    "budgeted_hours_mode",
}


def check_api_v1_projects_update_budgeted_hours_mode_error_component_attr(
    value: str,
) -> ApiV1ProjectsUpdateBudgetedHoursModeErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
