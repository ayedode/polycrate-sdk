from typing import Literal

ApiV1PricingProductsArchiveCreateConfigErrorComponentAttr = Literal["config"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsArchiveCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_pricing_products_archive_create_config_error_component_attr(
    value: str,
) -> ApiV1PricingProductsArchiveCreateConfigErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
