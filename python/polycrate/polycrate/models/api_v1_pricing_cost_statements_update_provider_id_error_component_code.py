from typing import Literal

ApiV1PricingCostStatementsUpdateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsUpdateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_cost_statements_update_provider_id_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsUpdateProviderIdErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
