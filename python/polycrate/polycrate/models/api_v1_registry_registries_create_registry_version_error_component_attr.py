from typing import Literal

ApiV1RegistryRegistriesCreateRegistryVersionErrorComponentAttr = Literal["registry_version"]

API_V1_REGISTRY_REGISTRIES_CREATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateRegistryVersionErrorComponentAttr
] = {
    "registry_version",
}


def check_api_v1_registry_registries_create_registry_version_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateRegistryVersionErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
