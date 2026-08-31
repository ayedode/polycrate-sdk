from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_pricing_quote_workspaces_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
