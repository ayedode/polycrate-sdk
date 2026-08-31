from typing import Literal

ApiV1PricingOrganizationProductsListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_organization_products_list_scope_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsListScopeErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
