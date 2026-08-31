from typing import Literal

ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_registry_registries_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
