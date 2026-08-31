from typing import Literal

ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_registry_registries_partial_update_credential_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateCredentialErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
