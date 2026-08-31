from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_worker_pools_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
