from typing import Literal

ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SUPPORT_PRODUCT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_quote_workspaces_create_support_product_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SUPPORT_PRODUCT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SUPPORT_PRODUCT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
