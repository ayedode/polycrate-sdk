from typing import Literal

ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_kubernetes_addon_config_revisions_archive_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsArchiveCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
