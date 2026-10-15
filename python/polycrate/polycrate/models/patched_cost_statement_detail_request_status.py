from typing import Literal

PatchedCostStatementDetailRequestStatus = Literal["draft", "final", "voided"]

PATCHED_COST_STATEMENT_DETAIL_REQUEST_STATUS_VALUES: set[PatchedCostStatementDetailRequestStatus] = {
    "draft",
    "final",
    "voided",
}


def check_patched_cost_statement_detail_request_status(value: str) -> PatchedCostStatementDetailRequestStatus:
    if value in PATCHED_COST_STATEMENT_DETAIL_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_COST_STATEMENT_DETAIL_REQUEST_STATUS_VALUES!r}"
    )
