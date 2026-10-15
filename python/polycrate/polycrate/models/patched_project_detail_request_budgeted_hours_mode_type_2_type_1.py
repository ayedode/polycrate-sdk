from typing import Literal

PatchedProjectDetailRequestBudgetedHoursModeType2Type1 = Literal["", "retainer", "tm"]

PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES: set[
    PatchedProjectDetailRequestBudgetedHoursModeType2Type1
] = {
    "",
    "retainer",
    "tm",
}


def check_patched_project_detail_request_budgeted_hours_mode_type_2_type_1(
    value: str,
) -> PatchedProjectDetailRequestBudgetedHoursModeType2Type1:
    if value in PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES!r}"
    )
