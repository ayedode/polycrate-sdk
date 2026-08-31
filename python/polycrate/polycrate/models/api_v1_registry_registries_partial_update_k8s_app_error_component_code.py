from typing import Literal

ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_registry_registries_partial_update_k8s_app_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateK8SAppErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
