from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponentAttr = Literal["location"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_LOCATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponentAttr
] = {
    "location",
}


def check_api_v1_kubernetes_worker_pools_partial_update_location_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_LOCATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_LOCATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
