from typing import Literal

CostStatementDetailEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

COST_STATEMENT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    CostStatementDetailEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_cost_statement_detail_effective_criticality_type_2_type_1(
    value: str,
) -> CostStatementDetailEffectiveCriticalityType2Type1:
    if value in COST_STATEMENT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
