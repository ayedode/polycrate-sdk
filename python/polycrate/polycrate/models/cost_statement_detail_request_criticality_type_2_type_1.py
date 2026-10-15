from typing import Literal

CostStatementDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[CostStatementDetailRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_cost_statement_detail_request_criticality_type_2_type_1(
    value: str,
) -> CostStatementDetailRequestCriticalityType2Type1:
    if value in COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
