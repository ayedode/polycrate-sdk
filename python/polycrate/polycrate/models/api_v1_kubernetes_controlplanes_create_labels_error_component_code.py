from typing import Literal

ApiV1KubernetesControlplanesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_controlplanes_create_labels_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateLabelsErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
