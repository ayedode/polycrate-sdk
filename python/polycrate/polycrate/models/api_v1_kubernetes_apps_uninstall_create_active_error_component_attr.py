from typing import Literal

ApiV1KubernetesAppsUninstallCreateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_apps_uninstall_create_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
