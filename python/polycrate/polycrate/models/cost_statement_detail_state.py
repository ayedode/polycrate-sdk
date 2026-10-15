from typing import Literal

CostStatementDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

COST_STATEMENT_DETAIL_STATE_VALUES: set[CostStatementDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_cost_statement_detail_state(value: str) -> CostStatementDetailState:
    if value in COST_STATEMENT_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_STATE_VALUES!r}")
