from typing import Literal

ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_pricing_cost_statements_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
