from typing import Literal

ApiV1PricingProductsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_products_update_kind_error_component_attr(
    value: str,
) -> ApiV1PricingProductsUpdateKindErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
