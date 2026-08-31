from typing import Literal

ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponentAttr = Literal["agreed_price"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponentAttr
] = {
    "agreed_price",
}


def check_api_v1_pricing_organization_products_create_agreed_price_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateAgreedPriceErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
