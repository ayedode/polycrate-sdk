from typing import Literal

ApiV1PricingOrganizationProductsListScopeErrorComponentAttr = Literal["scope"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_pricing_organization_products_list_scope_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsListScopeErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
