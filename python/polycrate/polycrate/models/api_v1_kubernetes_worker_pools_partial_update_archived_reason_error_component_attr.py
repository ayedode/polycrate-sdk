from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_kubernetes_worker_pools_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
