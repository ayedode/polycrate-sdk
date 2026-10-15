from typing import Literal

ProjectDetailRequestBudgetedHoursIntervalType1 = Literal[
    "", "day", "hour", "minute", "month", "project", "second", "year"
]

PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_1_VALUES: set[ProjectDetailRequestBudgetedHoursIntervalType1] = {
    "",
    "day",
    "hour",
    "minute",
    "month",
    "project",
    "second",
    "year",
}


def check_project_detail_request_budgeted_hours_interval_type_1(
    value: str,
) -> ProjectDetailRequestBudgetedHoursIntervalType1:
    if value in PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_1_VALUES!r}"
    )
