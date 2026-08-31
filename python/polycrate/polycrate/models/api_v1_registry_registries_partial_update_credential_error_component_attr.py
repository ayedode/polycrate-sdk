from typing import Literal

ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponentAttr = Literal["credential"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_registry_registries_partial_update_credential_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
