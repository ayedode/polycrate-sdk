from typing import Literal

ApiV1ProjectsUpdateBudgetedHoursErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsUpdateBudgetedHoursErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_projects_update_budgeted_hours_error_component_code(
    value: str,
) -> ApiV1ProjectsUpdateBudgetedHoursErrorComponentCode:
    if value in API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_BUDGETED_HOURS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
