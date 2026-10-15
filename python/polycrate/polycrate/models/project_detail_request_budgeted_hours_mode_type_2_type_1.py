from typing import Literal

ProjectDetailRequestBudgetedHoursModeType2Type1 = Literal["", "retainer", "tm"]

PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES: set[
    ProjectDetailRequestBudgetedHoursModeType2Type1
] = {
    "",
    "retainer",
    "tm",
}


def check_project_detail_request_budgeted_hours_mode_type_2_type_1(
    value: str,
) -> ProjectDetailRequestBudgetedHoursModeType2Type1:
    if value in PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_REQUEST_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES!r}"
    )
