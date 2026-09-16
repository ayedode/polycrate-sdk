from typing import Literal

ApiV1PricingProductsArchiveCreatePopErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_POP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsArchiveCreatePopErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_products_archive_create_pop_error_component_code(
    value: str,
) -> ApiV1PricingProductsArchiveCreatePopErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_POP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_POP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
