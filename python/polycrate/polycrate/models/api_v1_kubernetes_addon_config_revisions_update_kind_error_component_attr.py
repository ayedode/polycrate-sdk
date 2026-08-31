from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_addon_config_revisions_update_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
