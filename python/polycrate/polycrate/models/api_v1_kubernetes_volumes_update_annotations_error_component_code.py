from typing import Literal

ApiV1KubernetesVolumesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_VOLUMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_volumes_update_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
