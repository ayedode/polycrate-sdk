from typing import Literal

CostStatementDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

COST_STATEMENT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[CostStatementDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_cost_statement_detail_effective_criticality_type_1(
    value: str,
) -> CostStatementDetailEffectiveCriticalityType1:
    if value in COST_STATEMENT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
