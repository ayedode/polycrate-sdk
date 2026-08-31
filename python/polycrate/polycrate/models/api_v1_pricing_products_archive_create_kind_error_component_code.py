from typing import Literal

ApiV1PricingProductsArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_pricing_products_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1PricingProductsArchiveCreateKindErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
