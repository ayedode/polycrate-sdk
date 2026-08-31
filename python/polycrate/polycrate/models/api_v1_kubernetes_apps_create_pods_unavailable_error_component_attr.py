from typing import Literal

ApiV1KubernetesAppsCreatePodsUnavailableErrorComponentAttr = Literal["pods_unavailable"]

API_V1_KUBERNETES_APPS_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreatePodsUnavailableErrorComponentAttr
] = {
    "pods_unavailable",
}


def check_api_v1_kubernetes_apps_create_pods_unavailable_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreatePodsUnavailableErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_PODS_UNAVAILABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
