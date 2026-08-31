from typing import Literal

ApiV1PricingProductsUpdatePricePerUnitErrorComponentAttr = Literal["price_per_unit"]

API_V1_PRICING_PRODUCTS_UPDATE_PRICE_PER_UNIT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsUpdatePricePerUnitErrorComponentAttr
] = {
    "price_per_unit",
}


def check_api_v1_pricing_products_update_price_per_unit_error_component_attr(
    value: str,
) -> ApiV1PricingProductsUpdatePricePerUnitErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_PRICE_PER_UNIT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_PRICE_PER_UNIT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
