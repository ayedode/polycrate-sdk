from typing import Literal

ApiV1PricingProductsUpdateConfigErrorComponentAttr = Literal["config"]

API_V1_PRICING_PRODUCTS_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsUpdateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_pricing_products_update_config_error_component_attr(
    value: str,
) -> ApiV1PricingProductsUpdateConfigErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
