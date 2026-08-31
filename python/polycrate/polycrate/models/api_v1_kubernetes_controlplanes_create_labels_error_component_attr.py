from typing import Literal

ApiV1KubernetesControlplanesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_controlplanes_create_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
