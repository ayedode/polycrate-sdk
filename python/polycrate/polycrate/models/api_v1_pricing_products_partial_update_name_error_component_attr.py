from typing import Literal

ApiV1PricingProductsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_products_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingProductsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
