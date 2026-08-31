from typing import Literal

ApiV1ProjectsCreateBudgetedHoursErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PROJECTS_CREATE_BUDGETED_HOURS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsCreateBudgetedHoursErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_projects_create_budgeted_hours_error_component_code(
    value: str,
) -> ApiV1ProjectsCreateBudgetedHoursErrorComponentCode:
    if value in API_V1_PROJECTS_CREATE_BUDGETED_HOURS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_BUDGETED_HOURS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
