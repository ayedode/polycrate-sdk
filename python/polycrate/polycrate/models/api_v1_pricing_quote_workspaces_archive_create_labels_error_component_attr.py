from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_quote_workspaces_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
