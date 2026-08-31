from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_kubernetes_worker_pools_update_slo_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateSloTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
