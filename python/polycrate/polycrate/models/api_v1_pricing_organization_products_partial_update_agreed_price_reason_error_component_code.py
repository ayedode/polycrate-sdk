from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponentCode = Literal[
    "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponentCode
] = {
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_organization_products_partial_update_agreed_price_reason_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
