from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponentAttr = Literal["quote"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponentAttr
] = {
    "quote",
}


def check_api_v1_pricing_quote_workspaces_archive_create_quote_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
