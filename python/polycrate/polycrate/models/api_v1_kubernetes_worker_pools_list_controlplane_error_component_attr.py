from typing import Literal

ApiV1KubernetesWorkerPoolsListControlplaneErrorComponentAttr = Literal["controlplane"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_CONTROLPLANE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsListControlplaneErrorComponentAttr
] = {
    "controlplane",
}


def check_api_v1_kubernetes_worker_pools_list_controlplane_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListControlplaneErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_CONTROLPLANE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_CONTROLPLANE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
