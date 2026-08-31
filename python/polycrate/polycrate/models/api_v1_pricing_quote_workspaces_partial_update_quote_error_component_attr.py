from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponentAttr = Literal["quote"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponentAttr
] = {
    "quote",
}


def check_api_v1_pricing_quote_workspaces_partial_update_quote_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
