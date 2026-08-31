from typing import Literal

ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_archive_create_metadata_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateMetadataErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
