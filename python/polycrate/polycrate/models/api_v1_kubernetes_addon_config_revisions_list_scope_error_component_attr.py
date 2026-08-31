from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_addon_config_revisions_list_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
