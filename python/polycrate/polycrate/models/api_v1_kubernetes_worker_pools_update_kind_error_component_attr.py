from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_worker_pools_update_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
