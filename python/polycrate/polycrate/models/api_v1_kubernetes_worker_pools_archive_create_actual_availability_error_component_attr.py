from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_kubernetes_worker_pools_archive_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
