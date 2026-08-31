from typing import Literal

ApiV1KubernetesAppsUpdatePodsDetailsErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_UPDATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUpdatePodsDetailsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_update_pods_details_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUpdatePodsDetailsErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UPDATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_PODS_DETAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
