from typing import Literal

ApiV1KubernetesWorkerPoolsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_worker_pools_create_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
