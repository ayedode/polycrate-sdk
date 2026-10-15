from typing import Literal

CostStatementListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

COST_STATEMENT_LIST_STATE_VALUES: set[CostStatementListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_cost_statement_list_state(value: str) -> CostStatementListState:
    if value in COST_STATEMENT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_LIST_STATE_VALUES!r}")
