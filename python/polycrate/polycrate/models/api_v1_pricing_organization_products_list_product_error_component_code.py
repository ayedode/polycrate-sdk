from typing import Literal

ApiV1PricingOrganizationProductsListProductErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsListProductErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_pricing_organization_products_list_product_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsListProductErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
