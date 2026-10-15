from typing import Literal

CostStatementDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

COST_STATEMENT_DETAIL_LAST_STATE_VALUES: set[CostStatementDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_cost_statement_detail_last_state(value: str) -> CostStatementDetailLastState:
    if value in COST_STATEMENT_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_LAST_STATE_VALUES!r}")
