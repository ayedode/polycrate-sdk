from typing import Literal

ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_STORAGE_USED_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_registry_registries_archive_create_storage_used_bytes_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateStorageUsedBytesErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_STORAGE_USED_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_STORAGE_USED_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
