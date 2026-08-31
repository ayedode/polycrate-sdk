from typing import Literal

ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_TOTAL_NET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_pricing_cost_statements_partial_update_total_net_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_TOTAL_NET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_TOTAL_NET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
