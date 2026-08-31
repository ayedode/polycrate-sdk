from typing import Literal

ApiV1KubernetesControlplanesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_controlplanes_update_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
