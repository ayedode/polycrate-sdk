from typing import Literal

ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_registry_registries_partial_update_hostname_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateHostnameErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
