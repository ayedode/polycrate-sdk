from typing import Literal

ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_workspaces_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
