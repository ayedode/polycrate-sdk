from typing import Literal

ApiV1KubernetesVolumesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_VOLUMES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_volumes_update_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
