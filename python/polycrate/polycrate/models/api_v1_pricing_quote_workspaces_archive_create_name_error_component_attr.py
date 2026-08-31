from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_quote_workspaces_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
