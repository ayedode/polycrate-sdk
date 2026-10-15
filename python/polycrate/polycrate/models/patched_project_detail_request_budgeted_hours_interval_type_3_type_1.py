from typing import Literal

PatchedProjectDetailRequestBudgetedHoursIntervalType3Type1 = Literal[
    "", "day", "hour", "minute", "month", "project", "second", "year"
]

PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_3_TYPE_1_VALUES: set[
    PatchedProjectDetailRequestBudgetedHoursIntervalType3Type1
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


def check_patched_project_detail_request_budgeted_hours_interval_type_3_type_1(
    value: str,
) -> PatchedProjectDetailRequestBudgetedHoursIntervalType3Type1:
    if value in PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_INTERVAL_TYPE_3_TYPE_1_VALUES!r}"
    )
