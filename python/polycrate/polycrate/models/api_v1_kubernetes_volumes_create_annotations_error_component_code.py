from typing import Literal

ApiV1KubernetesVolumesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_VOLUMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_volumes_create_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesCreateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
