from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_worker_pools_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
