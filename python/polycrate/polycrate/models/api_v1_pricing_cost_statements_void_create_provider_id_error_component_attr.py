from typing import Literal

ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_pricing_cost_statements_void_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
