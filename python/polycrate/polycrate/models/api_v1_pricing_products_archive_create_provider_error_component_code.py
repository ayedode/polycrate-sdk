from typing import Literal

ApiV1PricingProductsArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_products_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1PricingProductsArchiveCreateProviderErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
