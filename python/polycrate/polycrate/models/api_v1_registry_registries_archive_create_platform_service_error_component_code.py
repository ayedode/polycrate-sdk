from typing import Literal

ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
