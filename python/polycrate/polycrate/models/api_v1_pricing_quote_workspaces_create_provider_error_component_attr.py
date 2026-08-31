from typing import Literal

ApiV1PricingQuoteWorkspacesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_quote_workspaces_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
