from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_worker_pools_partial_update_discovery_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
