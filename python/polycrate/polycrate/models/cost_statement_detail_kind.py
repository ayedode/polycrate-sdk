from typing import Literal

CostStatementDetailKind = Literal["generic"]

COST_STATEMENT_DETAIL_KIND_VALUES: set[CostStatementDetailKind] = {
    "generic",
}


def check_cost_statement_detail_kind(value: str) -> CostStatementDetailKind:
    if value in COST_STATEMENT_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_KIND_VALUES!r}")
