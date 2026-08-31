from typing import Literal

ApiV1PricingOrganizationProductsListProductKindErrorComponentAttr = Literal["product_kind"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsListProductKindErrorComponentAttr
] = {
    "product_kind",
}


def check_api_v1_pricing_organization_products_list_product_kind_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsListProductKindErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
