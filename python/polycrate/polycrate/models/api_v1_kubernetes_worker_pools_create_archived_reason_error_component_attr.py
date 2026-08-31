from typing import Literal

ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_kubernetes_worker_pools_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
