from typing import Literal

ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_BLOCK_STORAGE_PRODUCT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_quote_workspaces_create_block_storage_product_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_BLOCK_STORAGE_PRODUCT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_BLOCK_STORAGE_PRODUCT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
