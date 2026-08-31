from typing import Literal

ApiV1RegistryRegistriesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_update_archived_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesUpdateArchivedErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
