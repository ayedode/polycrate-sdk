from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_kubernetes_worker_pools_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
