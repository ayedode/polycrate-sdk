from typing import Literal

CostStatementDetailCriticalityType1 = Literal["", "high", "low", "medium"]

COST_STATEMENT_DETAIL_CRITICALITY_TYPE_1_VALUES: set[CostStatementDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_cost_statement_detail_criticality_type_1(value: str) -> CostStatementDetailCriticalityType1:
    if value in COST_STATEMENT_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_CRITICALITY_TYPE_1_VALUES!r}")
