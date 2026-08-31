from typing import Literal

ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_addon_config_revisions_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
