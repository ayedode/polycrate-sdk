from typing import Literal

ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_registry_registries_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
