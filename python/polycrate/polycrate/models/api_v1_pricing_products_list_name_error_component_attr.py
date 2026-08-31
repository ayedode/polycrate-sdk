from typing import Literal

ApiV1PricingProductsListNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_PRODUCTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingProductsListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_pricing_products_list_name_error_component_attr(
    value: str,
) -> ApiV1PricingProductsListNameErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
