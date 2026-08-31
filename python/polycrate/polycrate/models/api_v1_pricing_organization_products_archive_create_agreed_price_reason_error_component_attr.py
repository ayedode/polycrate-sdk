from typing import Literal

ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponentAttr = Literal["agreed_price_reason"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponentAttr
] = {
    "agreed_price_reason",
}


def check_api_v1_pricing_organization_products_archive_create_agreed_price_reason_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsArchiveCreateAgreedPriceReasonErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_ARCHIVE_CREATE_AGREED_PRICE_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
