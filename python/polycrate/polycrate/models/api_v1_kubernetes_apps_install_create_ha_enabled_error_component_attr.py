from typing import Literal

ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponentAttr = Literal["ha_enabled"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponentAttr
] = {
    "ha_enabled",
}


def check_api_v1_kubernetes_apps_install_create_ha_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateHaEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_HA_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
