from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_kubernetes_worker_pools_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
