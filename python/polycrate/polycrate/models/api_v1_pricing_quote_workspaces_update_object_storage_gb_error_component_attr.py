from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponentAttr = Literal["object_storage_gb"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_OBJECT_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponentAttr
] = {
    "object_storage_gb",
}


def check_api_v1_pricing_quote_workspaces_update_object_storage_gb_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_OBJECT_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_OBJECT_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
