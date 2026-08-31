from typing import Literal

ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponentAttr = Literal["addon"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_ADDON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponentAttr
] = {
    "addon",
}


def check_api_v1_kubernetes_addon_config_revisions_partial_update_addon_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_ADDON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_ADDON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
