from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quote_workspaces_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
