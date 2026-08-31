from typing import Literal

ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponentAttr = Literal["agreed_price_reason"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponentAttr
] = {
    "agreed_price_reason",
}


def check_api_v1_pricing_organization_products_create_agreed_price_reason_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateAgreedPriceReasonErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
