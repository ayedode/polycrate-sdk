from typing import Literal

ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponentAttr = Literal["registry_version"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponentAttr
] = {
    "registry_version",
}


def check_api_v1_registry_registries_partial_update_registry_version_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
