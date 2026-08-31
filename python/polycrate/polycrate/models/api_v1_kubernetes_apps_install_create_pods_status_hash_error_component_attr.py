from typing import Literal

ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponentAttr = Literal["pods_status_hash"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponentAttr
] = {
    "pods_status_hash",
}


def check_api_v1_kubernetes_apps_install_create_pods_status_hash_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
