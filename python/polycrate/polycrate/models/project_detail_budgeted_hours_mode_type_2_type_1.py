from typing import Literal

ProjectDetailBudgetedHoursModeType2Type1 = Literal["", "retainer", "tm"]

PROJECT_DETAIL_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES: set[ProjectDetailBudgetedHoursModeType2Type1] = {
    "",
    "retainer",
    "tm",
}


def check_project_detail_budgeted_hours_mode_type_2_type_1(value: str) -> ProjectDetailBudgetedHoursModeType2Type1:
    if value in PROJECT_DETAIL_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_BUDGETED_HOURS_MODE_TYPE_2_TYPE_1_VALUES!r}"
    )
