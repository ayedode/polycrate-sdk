from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_addon_config_revisions_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
