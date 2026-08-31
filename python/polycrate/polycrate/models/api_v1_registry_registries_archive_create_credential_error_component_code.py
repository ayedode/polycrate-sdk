from typing import Literal

ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_registry_registries_archive_create_credential_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateCredentialErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
