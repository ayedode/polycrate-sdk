from typing import Literal

ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_kubernetes_apps_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
