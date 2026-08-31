from typing import Literal

ApiV1KubernetesControlplanesCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_controlplanes_create_provider_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateProviderErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
