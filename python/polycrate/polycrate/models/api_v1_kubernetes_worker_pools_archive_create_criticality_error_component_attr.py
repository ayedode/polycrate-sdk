from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_worker_pools_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
