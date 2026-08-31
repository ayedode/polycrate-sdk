from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponentAttr = Literal["quote"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponentAttr
] = {
    "quote",
}


def check_api_v1_pricing_quote_workspaces_update_quote_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_QUOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
