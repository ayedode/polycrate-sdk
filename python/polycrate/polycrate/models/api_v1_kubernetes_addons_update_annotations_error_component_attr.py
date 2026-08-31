from typing import Literal

ApiV1KubernetesAddonsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_ADDONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_addons_update_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
