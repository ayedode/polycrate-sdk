from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponentAttr = Literal["object_storage_product"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_OBJECT_STORAGE_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponentAttr
] = {
    "object_storage_product",
}


def check_api_v1_pricing_quote_workspaces_archive_create_object_storage_product_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_OBJECT_STORAGE_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_OBJECT_STORAGE_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
