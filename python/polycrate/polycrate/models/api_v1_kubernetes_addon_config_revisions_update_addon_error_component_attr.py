from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponentAttr = Literal["addon"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ADDON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponentAttr
] = {
    "addon",
}


def check_api_v1_kubernetes_addon_config_revisions_update_addon_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateAddonErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ADDON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_ADDON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
