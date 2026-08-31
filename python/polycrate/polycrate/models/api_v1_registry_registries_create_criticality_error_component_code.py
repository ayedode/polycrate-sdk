from typing import Literal

ApiV1RegistryRegistriesCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_REGISTRY_REGISTRIES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_registry_registries_create_criticality_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateCriticalityErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
