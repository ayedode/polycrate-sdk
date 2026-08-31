from typing import Literal

ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOST_PRODUCT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_quote_workspaces_create_host_product_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOST_PRODUCT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOST_PRODUCT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
