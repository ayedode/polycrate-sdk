from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_kubernetes_worker_pools_update_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
