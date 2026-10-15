from typing import Literal

CostStatementDetailCriticalityType2Type1 = Literal["", "high", "low", "medium"]

COST_STATEMENT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CostStatementDetailCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_cost_statement_detail_criticality_type_2_type_1(value: str) -> CostStatementDetailCriticalityType2Type1:
    if value in COST_STATEMENT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
