from typing import Literal

ApiV1RegistryRegistriesCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_REGISTRY_REGISTRIES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_registry_registries_create_metadata_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateMetadataErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
