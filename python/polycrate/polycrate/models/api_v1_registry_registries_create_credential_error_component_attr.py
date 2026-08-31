from typing import Literal

ApiV1RegistryRegistriesCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_REGISTRY_REGISTRIES_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_registry_registries_create_credential_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateCredentialErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
