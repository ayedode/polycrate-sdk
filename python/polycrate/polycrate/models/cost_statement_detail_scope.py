from typing import Literal

CostStatementDetailScope = Literal["system", "user"]

COST_STATEMENT_DETAIL_SCOPE_VALUES: set[CostStatementDetailScope] = {
    "system",
    "user",
}


def check_cost_statement_detail_scope(value: str) -> CostStatementDetailScope:
    if value in COST_STATEMENT_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_SCOPE_VALUES!r}")
