from typing import Literal

ApiV1PricingCostStatementsUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_cost_statements_update_provider_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsUpdateProviderErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
