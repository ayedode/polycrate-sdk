from typing import Literal

ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_KUBERNETES_APPS_UPDATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_apps_update_pods_status_updated_at_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdatePodsStatusUpdatedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_PODS_STATUS_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
