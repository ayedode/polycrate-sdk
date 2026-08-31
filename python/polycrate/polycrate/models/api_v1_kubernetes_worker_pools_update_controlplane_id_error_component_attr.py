from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponentAttr = Literal["controlplane_id"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CONTROLPLANE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponentAttr
] = {
    "controlplane_id",
}


def check_api_v1_kubernetes_worker_pools_update_controlplane_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateControlplaneIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CONTROLPLANE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CONTROLPLANE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
