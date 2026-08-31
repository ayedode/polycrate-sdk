from typing import Literal

ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_worker_pools_create_archived_at_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateArchivedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
