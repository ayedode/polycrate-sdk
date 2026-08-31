from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_pricing_quote_workspaces_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
