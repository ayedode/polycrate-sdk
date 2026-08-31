from typing import Literal

ApiV1PricingCostStatementsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_cost_statements_update_provider_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateProviderErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
