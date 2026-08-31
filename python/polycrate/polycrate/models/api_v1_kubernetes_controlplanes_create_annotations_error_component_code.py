from typing import Literal

ApiV1KubernetesControlplanesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_controlplanes_create_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesCreateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
