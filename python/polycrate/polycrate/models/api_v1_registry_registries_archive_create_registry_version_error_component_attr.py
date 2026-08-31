from typing import Literal

ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponentAttr = Literal["registry_version"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponentAttr
] = {
    "registry_version",
}


def check_api_v1_registry_registries_archive_create_registry_version_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateRegistryVersionErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_REGISTRY_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
