from typing import Literal

ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_registry_registries_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
