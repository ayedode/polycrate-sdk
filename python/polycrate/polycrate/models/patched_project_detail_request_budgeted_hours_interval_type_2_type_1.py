from typing import Literal

PatchedProjectDetailRequestBudgetedHoursIntervalType2Type1 = Literal[
    "", "day", "hour", "minute", "month", "project", "second", "year"
]

PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_2_TYPE_1_VALUES: set[
    PatchedProjectDetailRequestBudgetedHoursIntervalType2Type1
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


def check_patched_project_detail_request_budgeted_hours_interval_type_2_type_1(
    value: str,
) -> PatchedProjectDetailRequestBudgetedHoursIntervalType2Type1:
    if value in PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_2_TYPE_1_VALUES!r}"
    )
