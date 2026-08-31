from typing import Literal

ApiV1RegistryRegistriesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_REGISTRY_REGISTRIES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_registry_registries_list_state_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesListStateErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
