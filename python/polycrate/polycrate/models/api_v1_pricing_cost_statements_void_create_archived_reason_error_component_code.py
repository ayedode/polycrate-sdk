from typing import Literal

ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_cost_statements_void_create_archived_reason_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
