from typing import Literal

CostStatementDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

COST_STATEMENT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[CostStatementDetailCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_cost_statement_detail_criticality_type_3_type_1(value: str) -> CostStatementDetailCriticalityType3Type1:
    if value in COST_STATEMENT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
