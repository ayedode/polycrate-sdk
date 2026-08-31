from typing import Literal

ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_quote_workspaces_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
