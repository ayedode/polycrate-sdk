from typing import Literal

ApiV1PricingProductsCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_products_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
