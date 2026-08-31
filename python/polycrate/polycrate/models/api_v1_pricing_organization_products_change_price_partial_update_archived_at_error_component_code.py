from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_archived_at_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdateArchivedAtErrorComponentCode:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
