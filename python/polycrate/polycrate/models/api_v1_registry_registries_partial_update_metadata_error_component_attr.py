from typing import Literal

ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_registry_registries_partial_update_metadata_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateMetadataErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
