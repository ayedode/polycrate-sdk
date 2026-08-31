from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponentAttr = Literal["label"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LABEL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponentAttr
] = {
    "label",
}


def check_api_v1_pricing_quote_workspaces_archive_create_label_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LABEL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LABEL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
