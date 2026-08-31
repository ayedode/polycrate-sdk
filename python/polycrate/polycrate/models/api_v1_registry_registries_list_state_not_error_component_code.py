from typing import Literal

ApiV1RegistryRegistriesListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_REGISTRY_REGISTRIES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesListStateNotErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_registry_registries_list_state_not_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesListStateNotErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
