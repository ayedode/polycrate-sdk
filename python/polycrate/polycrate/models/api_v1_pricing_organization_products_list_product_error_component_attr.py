from typing import Literal

ApiV1PricingOrganizationProductsListProductErrorComponentAttr = Literal["product"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsListProductErrorComponentAttr
] = {
    "product",
}


def check_api_v1_pricing_organization_products_list_product_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsListProductErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
