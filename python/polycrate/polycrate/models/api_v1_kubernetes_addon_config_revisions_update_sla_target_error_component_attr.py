from typing import Literal

ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_kubernetes_addon_config_revisions_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
