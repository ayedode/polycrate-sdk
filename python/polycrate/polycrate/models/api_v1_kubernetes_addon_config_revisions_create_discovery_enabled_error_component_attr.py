from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_kubernetes_addon_config_revisions_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
