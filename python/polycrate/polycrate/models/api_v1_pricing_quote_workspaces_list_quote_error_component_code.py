from typing import Literal

ApiV1PricingQuoteWorkspacesListQuoteErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_QUOTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesListQuoteErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_pricing_quote_workspaces_list_quote_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesListQuoteErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_QUOTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_QUOTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
