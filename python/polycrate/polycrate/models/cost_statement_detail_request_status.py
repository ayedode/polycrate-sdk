from typing import Literal

CostStatementDetailRequestStatus = Literal["draft", "final", "voided"]

COST_STATEMENT_DETAIL_REQUEST_STATUS_VALUES: set[CostStatementDetailRequestStatus] = {
    "draft",
    "final",
    "voided",
}


def check_cost_statement_detail_request_status(value: str) -> CostStatementDetailRequestStatus:
    if value in COST_STATEMENT_DETAIL_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_REQUEST_STATUS_VALUES!r}")
