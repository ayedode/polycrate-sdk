from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null", "required"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
    "required",
}


def check_api_v1_pricing_organization_products_partial_update_agreed_price_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
