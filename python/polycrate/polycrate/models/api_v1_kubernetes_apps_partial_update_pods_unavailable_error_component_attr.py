from typing import Literal

ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponentAttr = Literal["pods_unavailable"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponentAttr
] = {
    "pods_unavailable",
}


def check_api_v1_kubernetes_apps_partial_update_pods_unavailable_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdatePodsUnavailableErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
