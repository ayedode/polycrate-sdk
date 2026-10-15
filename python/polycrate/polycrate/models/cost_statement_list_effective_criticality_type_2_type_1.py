from typing import Literal

CostStatementListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

COST_STATEMENT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CostStatementListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_cost_statement_list_effective_criticality_type_2_type_1(
    value: str,
) -> CostStatementListEffectiveCriticalityType2Type1:
    if value in COST_STATEMENT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
