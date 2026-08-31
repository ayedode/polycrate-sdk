from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponentAttr = Literal["agreed_price"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponentAttr
] = {
    "agreed_price",
}


def check_api_v1_pricing_organization_products_partial_update_agreed_price_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
