from typing import Literal

ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponentAttr = Literal["pods_status_updated_at"]

API_V1_KUBERNETES_APPS_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponentAttr
] = {
    "pods_status_updated_at",
}


def check_api_v1_kubernetes_apps_create_pods_status_updated_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreatePodsStatusUpdatedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
