from typing import Literal

ApiV1KubernetesVolumesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_VOLUMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_volumes_update_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
