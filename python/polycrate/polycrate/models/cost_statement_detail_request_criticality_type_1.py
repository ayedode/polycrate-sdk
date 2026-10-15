from typing import Literal

CostStatementDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[CostStatementDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_cost_statement_detail_request_criticality_type_1(value: str) -> CostStatementDetailRequestCriticalityType1:
    if value in COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
