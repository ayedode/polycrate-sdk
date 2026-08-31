from typing import Literal

ApiV1RegistryRegistriesCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateDebugModeErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
