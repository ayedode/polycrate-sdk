from typing import Literal

ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponentAttr = Literal["last_installation"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponentAttr
] = {
    "last_installation",
}


def check_api_v1_kubernetes_apps_install_create_last_installation_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateLastInstallationErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
