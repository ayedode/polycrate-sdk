from typing import Literal

ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponentAttr = Literal["budgeted_hours"]

API_V1_PROJECTS_ARCHIVE_CREATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponentAttr
] = {
    "budgeted_hours",
}


def check_api_v1_projects_archive_create_budgeted_hours_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreateBudgetedHoursErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_BUDGETED_HOURS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
