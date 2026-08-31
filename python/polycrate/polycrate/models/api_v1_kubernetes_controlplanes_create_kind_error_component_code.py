from typing import Literal

ApiV1KubernetesControlplanesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_controlplanes_create_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateKindErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
