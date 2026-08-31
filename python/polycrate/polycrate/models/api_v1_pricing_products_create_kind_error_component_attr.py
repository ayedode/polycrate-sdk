from typing import Literal

ApiV1PricingProductsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_PRODUCTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_products_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
