from typing import Literal

ApiV1PricingProductsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_PRICING_PRODUCTS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_pricing_products_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1PricingProductsListUpdatedAtErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
