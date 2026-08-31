from typing import Literal

ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_products_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingProductsArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
