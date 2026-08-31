from typing import Literal

ApiV1PricingCostStatementsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_cost_statements_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
