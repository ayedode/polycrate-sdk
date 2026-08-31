from typing import Literal

ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponentAttr = Literal["support_product"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SUPPORT_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponentAttr
] = {
    "support_product",
}


def check_api_v1_pricing_quote_workspaces_create_support_product_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SUPPORT_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_SUPPORT_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
