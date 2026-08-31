from typing import Literal

ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_OBJECT_STORAGE_PRODUCT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_pricing_quote_workspaces_create_object_storage_product_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_OBJECT_STORAGE_PRODUCT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_OBJECT_STORAGE_PRODUCT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
