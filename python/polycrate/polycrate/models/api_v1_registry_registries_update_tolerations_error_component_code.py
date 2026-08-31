from typing import Literal

ApiV1RegistryRegistriesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_update_tolerations_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesUpdateTolerationsErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
