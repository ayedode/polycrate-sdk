from typing import Literal

ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_addon_config_revisions_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
