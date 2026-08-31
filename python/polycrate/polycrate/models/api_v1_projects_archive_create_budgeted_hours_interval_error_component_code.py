from typing import Literal

ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponentCode = Literal["invalid_choice"]

API_V1_PROJECTS_ARCHIVE_CREATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_projects_archive_create_budgeted_hours_interval_error_component_code(
    value: str,
) -> ApiV1ProjectsArchiveCreateBudgetedHoursIntervalErrorComponentCode:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_BUDGETED_HOURS_INTERVAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
