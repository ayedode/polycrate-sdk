from typing import Literal

CostStatementStatusEnum = Literal["draft", "final", "voided"]

COST_STATEMENT_STATUS_ENUM_VALUES: set[CostStatementStatusEnum] = {
    "draft",
    "final",
    "voided",
}


def check_cost_statement_status_enum(value: str) -> CostStatementStatusEnum:
    if value in COST_STATEMENT_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COST_STATEMENT_STATUS_ENUM_VALUES!r}")
