from typing import Literal

ApiV1PricingProductsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_create_archived_error_component_code(
    value: str,
) -> ApiV1PricingProductsCreateArchivedErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
