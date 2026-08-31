from typing import Literal

ApiV1PricingQuoteWorkspacesCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quote_workspaces_create_provider_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateProviderErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
