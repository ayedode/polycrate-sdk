from typing import Literal

ApiV1PricingCostStatementsCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_pricing_cost_statements_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
