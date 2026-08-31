from typing import Literal

ApiV1RegistryRegistriesCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_create_metadata_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateMetadataErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
