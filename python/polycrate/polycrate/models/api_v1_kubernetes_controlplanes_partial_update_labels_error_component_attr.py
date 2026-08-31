from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_controlplanes_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
