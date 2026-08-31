from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponentAttr = Literal["label"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LABEL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponentAttr
] = {
    "label",
}


def check_api_v1_pricing_quote_workspaces_partial_update_label_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LABEL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LABEL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
