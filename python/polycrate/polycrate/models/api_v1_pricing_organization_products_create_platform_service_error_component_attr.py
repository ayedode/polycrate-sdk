from typing import Literal

ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_organization_products_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
