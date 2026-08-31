from typing import Literal

ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponentAttr = Literal["host_product"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponentAttr
] = {
    "host_product",
}


def check_api_v1_pricing_quote_workspaces_create_host_product_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOST_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
