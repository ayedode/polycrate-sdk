from typing import Literal

ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_pricing_cost_statements_void_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
