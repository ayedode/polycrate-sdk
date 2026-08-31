from typing import Literal

ApiV1KubernetesVolumesListK8SAppErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_KUBERNETES_VOLUMES_LIST_K8S_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesListK8SAppErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_list_k8s_app_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesListK8SAppErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_K8S_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_K8S_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
