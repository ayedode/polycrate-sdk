from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_quote_workspaces_update_provider_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
