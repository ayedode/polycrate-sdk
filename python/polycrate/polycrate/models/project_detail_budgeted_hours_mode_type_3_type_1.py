from typing import Literal

ProjectDetailBudgetedHoursModeType3Type1 = Literal["", "retainer", "tm"]

PROJECT_DETAIL_BUDGETED_HOURS_MODE_TYPE_3_TYPE_1_VALUES: set[ProjectDetailBudgetedHoursModeType3Type1] = {
    "",
    "retainer",
    "tm",
}


def check_project_detail_budgeted_hours_mode_type_3_type_1(value: str) -> ProjectDetailBudgetedHoursModeType3Type1:
    if value in PROJECT_DETAIL_BUDGETED_HOURS_MODE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_BUDGETED_HOURS_MODE_TYPE_3_TYPE_1_VALUES!r}"
    )
