from typing import Literal

ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponentAttr = Literal["version"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_kubernetes_addon_config_revisions_partial_update_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
