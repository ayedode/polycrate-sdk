from typing import Literal

ApiV1KubernetesAppsUninstallCreateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_apps_uninstall_create_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
