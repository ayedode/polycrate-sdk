from typing import Literal

ApiV1RegistryRegistriesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_create_tolerations_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateTolerationsErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
