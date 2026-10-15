from typing import Literal

PatchedCostStatementDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedCostStatementDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_cost_statement_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedCostStatementDetailRequestCriticalityType3Type1:
    if value in PATCHED_COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_COST_STATEMENT_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
