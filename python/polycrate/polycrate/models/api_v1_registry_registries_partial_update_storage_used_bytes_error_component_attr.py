from typing import Literal

ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponentAttr = Literal["storage_used_bytes"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_STORAGE_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponentAttr
] = {
    "storage_used_bytes",
}


def check_api_v1_registry_registries_partial_update_storage_used_bytes_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateStorageUsedBytesErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_STORAGE_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_STORAGE_USED_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
