from typing import Literal

ApiV1KubernetesAppsCreateUninstalledErrorComponentAttr = Literal["uninstalled"]

API_V1_KUBERNETES_APPS_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateUninstalledErrorComponentAttr
] = {
    "uninstalled",
}


def check_api_v1_kubernetes_apps_create_uninstalled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateUninstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
