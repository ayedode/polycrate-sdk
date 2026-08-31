from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponentAttr = Literal["agreed_price"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponentAttr
] = {
    "agreed_price",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_agreed_price_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceErrorComponentAttr:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
