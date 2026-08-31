from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null", "required"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AGREED_PRICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
    "required",
}


def check_api_v1_pricing_organization_products_archive_create_agreed_price_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AGREED_PRICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AGREED_PRICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
