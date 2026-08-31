from typing import Literal

ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_registry_registries_archive_create_hostname_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
