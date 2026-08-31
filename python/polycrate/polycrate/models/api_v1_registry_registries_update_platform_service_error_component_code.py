from typing import Literal

ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_update_platform_service_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
