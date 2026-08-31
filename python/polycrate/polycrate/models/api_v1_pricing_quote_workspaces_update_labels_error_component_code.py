from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_quote_workspaces_update_labels_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
