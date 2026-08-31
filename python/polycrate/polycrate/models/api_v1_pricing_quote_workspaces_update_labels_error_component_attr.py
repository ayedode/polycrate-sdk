from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_quote_workspaces_update_labels_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
