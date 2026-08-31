from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_quote_workspaces_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
