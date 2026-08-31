from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponentAttr = Literal["agreed_price_reason"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponentAttr
] = {
    "agreed_price_reason",
}


def check_api_v1_pricing_organization_products_partial_update_agreed_price_reason_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateAgreedPriceReasonErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
