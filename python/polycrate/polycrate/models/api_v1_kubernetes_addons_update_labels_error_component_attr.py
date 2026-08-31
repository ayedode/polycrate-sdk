from typing import Literal

ApiV1KubernetesAddonsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_ADDONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_addons_update_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
