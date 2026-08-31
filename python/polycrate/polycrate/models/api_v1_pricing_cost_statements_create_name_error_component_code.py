from typing import Literal

ApiV1PricingCostStatementsCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_COST_STATEMENTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsCreateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_cost_statements_create_name_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsCreateNameErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
