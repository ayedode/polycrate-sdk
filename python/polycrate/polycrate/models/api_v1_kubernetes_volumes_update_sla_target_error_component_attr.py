from typing import Literal

ApiV1KubernetesVolumesUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_KUBERNETES_VOLUMES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_kubernetes_volumes_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
