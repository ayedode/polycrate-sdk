from typing import Literal

ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_worker_pools_create_archived_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateArchivedErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
