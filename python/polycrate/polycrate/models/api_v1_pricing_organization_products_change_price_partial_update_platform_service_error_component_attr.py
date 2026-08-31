from typing import Literal

ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_organization_products_change_price_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsChangePricePartialUpdatePlatformServiceErrorComponentAttr:
    if (
        value
        in API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CHANGE_PRICE_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
