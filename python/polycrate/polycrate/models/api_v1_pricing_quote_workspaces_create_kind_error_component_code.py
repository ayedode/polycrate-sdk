from typing import Literal

ApiV1PricingQuoteWorkspacesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_quote_workspaces_create_kind_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateKindErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
