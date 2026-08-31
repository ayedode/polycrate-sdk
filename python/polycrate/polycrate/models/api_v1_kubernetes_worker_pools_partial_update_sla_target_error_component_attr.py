from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_kubernetes_worker_pools_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
