from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponentAttr = Literal[
    "agreed_price_reason"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponentAttr
] = {
    "agreed_price_reason",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_agreed_price_reason_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateAgreedPriceReasonErrorComponentAttr:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
