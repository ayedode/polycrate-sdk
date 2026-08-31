from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_kubernetes_worker_pools_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
