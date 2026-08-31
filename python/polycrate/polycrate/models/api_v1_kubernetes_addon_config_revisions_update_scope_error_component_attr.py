from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_addon_config_revisions_update_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
