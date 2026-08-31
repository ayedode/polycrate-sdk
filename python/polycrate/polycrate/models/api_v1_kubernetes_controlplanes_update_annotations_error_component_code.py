from typing import Literal

ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_controlplanes_update_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
