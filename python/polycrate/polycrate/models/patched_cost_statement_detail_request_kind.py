from typing import Literal

PatchedCostStatementDetailRequestKind = Literal["generic"]

PATCHED_COST_STATEMENT_DETAIL_REQUEST_KIND_VALUES: set[PatchedCostStatementDetailRequestKind] = {
    "generic",
}


def check_patched_cost_statement_detail_request_kind(value: str) -> PatchedCostStatementDetailRequestKind:
    if value in PATCHED_COST_STATEMENT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_COST_STATEMENT_DETAIL_REQUEST_KIND_VALUES!r}"
    )
