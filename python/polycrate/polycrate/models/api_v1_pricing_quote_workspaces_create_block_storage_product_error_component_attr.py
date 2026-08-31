from typing import Literal

ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponentAttr = Literal["block_storage_product"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_BLOCK_STORAGE_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponentAttr
] = {
    "block_storage_product",
}


def check_api_v1_pricing_quote_workspaces_create_block_storage_product_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_BLOCK_STORAGE_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_BLOCK_STORAGE_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
