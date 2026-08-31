from typing import Literal

ApiV1PricingProductsCreateConfigErrorComponentAttr = Literal["config"]

API_V1_PRICING_PRODUCTS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_pricing_products_create_config_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateConfigErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
