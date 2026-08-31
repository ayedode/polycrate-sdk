from typing import Literal

ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_quote_workspaces_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
