from typing import Literal

ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_kubernetes_worker_pools_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
