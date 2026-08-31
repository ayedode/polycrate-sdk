from typing import Literal

ApiV1KubernetesAddonsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_ADDONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_addons_create_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
