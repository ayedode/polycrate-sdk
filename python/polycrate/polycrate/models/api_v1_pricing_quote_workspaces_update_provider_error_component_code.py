from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quote_workspaces_update_provider_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
