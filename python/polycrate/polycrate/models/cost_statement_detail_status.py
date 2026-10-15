from typing import Literal

CostStatementDetailStatus = Literal["draft", "final", "voided"]

COST_STATEMENT_DETAIL_STATUS_VALUES: set[CostStatementDetailStatus] = {
    "draft",
    "final",
    "voided",
}


def check_cost_statement_detail_status(value: str) -> CostStatementDetailStatus:
    if value in COST_STATEMENT_DETAIL_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_STATUS_VALUES!r}")
