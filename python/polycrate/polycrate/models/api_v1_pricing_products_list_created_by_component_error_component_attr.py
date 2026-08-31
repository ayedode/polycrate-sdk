from typing import Literal

ApiV1PricingProductsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_PRICING_PRODUCTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_pricing_products_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1PricingProductsListCreatedByComponentErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
