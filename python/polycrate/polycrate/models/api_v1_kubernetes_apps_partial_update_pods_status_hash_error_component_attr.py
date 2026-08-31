from typing import Literal

ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponentAttr = Literal["pods_status_hash"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponentAttr
] = {
    "pods_status_hash",
}


def check_api_v1_kubernetes_apps_partial_update_pods_status_hash_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdatePodsStatusHashErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
