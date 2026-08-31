from typing import Literal

ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponentAttr = Literal["installation_failed"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponentAttr
] = {
    "installation_failed",
}


def check_api_v1_kubernetes_apps_install_create_installation_failed_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateInstallationFailedErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
