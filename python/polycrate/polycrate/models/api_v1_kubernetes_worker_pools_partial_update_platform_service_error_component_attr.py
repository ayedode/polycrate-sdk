from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_kubernetes_worker_pools_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
