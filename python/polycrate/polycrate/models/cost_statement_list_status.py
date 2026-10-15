from typing import Literal

CostStatementListStatus = Literal["draft", "final", "voided"]

COST_STATEMENT_LIST_STATUS_VALUES: set[CostStatementListStatus] = {
    "draft",
    "final",
    "voided",
}


def check_cost_statement_list_status(value: str) -> CostStatementListStatus:
    if value in COST_STATEMENT_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_LIST_STATUS_VALUES!r}")
