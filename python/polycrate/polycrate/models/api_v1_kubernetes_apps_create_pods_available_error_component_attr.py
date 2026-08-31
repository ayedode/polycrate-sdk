from typing import Literal

ApiV1KubernetesAppsCreatePodsAvailableErrorComponentAttr = Literal["pods_available"]

API_V1_KUBERNETES_APPS_CREATE_PODS_AVAILABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreatePodsAvailableErrorComponentAttr
] = {
    "pods_available",
}


def check_api_v1_kubernetes_apps_create_pods_available_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreatePodsAvailableErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_PODS_AVAILABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_PODS_AVAILABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
