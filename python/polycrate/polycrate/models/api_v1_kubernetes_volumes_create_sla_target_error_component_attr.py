from typing import Literal

ApiV1KubernetesVolumesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_KUBERNETES_VOLUMES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_kubernetes_volumes_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
