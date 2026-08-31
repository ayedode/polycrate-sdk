from typing import Literal

ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_kubernetes_apps_install_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
