from typing import Literal

ProjectDetailRequestBudgetedHoursIntervalType2Type1 = Literal[
    "", "day", "hour", "minute", "month", "project", "second", "year"
]

PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_2_TYPE_1_VALUES: set[
    ProjectDetailRequestBudgetedHoursIntervalType2Type1
] = {
    "",
    "day",
    "hour",
    "minute",
    "month",
    "project",
    "second",
    "year",
}


def check_project_detail_request_budgeted_hours_interval_type_2_type_1(
    value: str,
) -> ProjectDetailRequestBudgetedHoursIntervalType2Type1:
    if value in PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_2_TYPE_1_VALUES!r}"
    )
