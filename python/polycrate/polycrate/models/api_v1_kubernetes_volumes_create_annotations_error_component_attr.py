from typing import Literal

ApiV1KubernetesVolumesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_VOLUMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_volumes_create_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
