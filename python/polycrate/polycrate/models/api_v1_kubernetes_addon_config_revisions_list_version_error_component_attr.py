from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponentAttr = Literal["version"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_kubernetes_addon_config_revisions_list_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
