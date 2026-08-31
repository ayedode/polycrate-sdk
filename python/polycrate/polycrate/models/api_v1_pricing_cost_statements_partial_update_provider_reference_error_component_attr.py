from typing import Literal

ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_pricing_cost_statements_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
