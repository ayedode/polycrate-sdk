from typing import Literal

CostStatementDetailRequestKind = Literal["generic"]

COST_STATEMENT_DETAIL_REQUEST_KIND_VALUES: set[CostStatementDetailRequestKind] = {
    "generic",
}


def check_cost_statement_detail_request_kind(value: str) -> CostStatementDetailRequestKind:
    if value in COST_STATEMENT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_REQUEST_KIND_VALUES!r}")
