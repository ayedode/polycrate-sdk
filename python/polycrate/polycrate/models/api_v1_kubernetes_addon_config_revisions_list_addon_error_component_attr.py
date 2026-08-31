from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponentAttr = Literal["addon"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_ADDON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponentAttr
] = {
    "addon",
}


def check_api_v1_kubernetes_addon_config_revisions_list_addon_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListAddonErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_ADDON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_ADDON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
