from typing import Literal

ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_workspaces_create_platform_service_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
