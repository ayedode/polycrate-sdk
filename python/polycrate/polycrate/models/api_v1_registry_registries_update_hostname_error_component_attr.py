from typing import Literal

ApiV1RegistryRegistriesUpdateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_REGISTRY_REGISTRIES_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesUpdateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_registry_registries_update_hostname_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesUpdateHostnameErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
