from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_workspaces_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
