from typing import Literal

ApiV1PricingQuoteWorkspacesListQuoteErrorComponentAttr = Literal["quote"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_QUOTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesListQuoteErrorComponentAttr
] = {
    "quote",
}


def check_api_v1_pricing_quote_workspaces_list_quote_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesListQuoteErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_QUOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_QUOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
