from typing import Literal

ApiV1PricingProductsArchiveCreatePopErrorComponentAttr = Literal["pop"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_POP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsArchiveCreatePopErrorComponentAttr
] = {
    "pop",
}


def check_api_v1_pricing_products_archive_create_pop_error_component_attr(
    value: str,
) -> ApiV1PricingProductsArchiveCreatePopErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_POP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_POP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
