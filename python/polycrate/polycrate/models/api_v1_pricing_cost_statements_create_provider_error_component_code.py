from typing import Literal

ApiV1PricingCostStatementsCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_cost_statements_create_provider_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsCreateProviderErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
