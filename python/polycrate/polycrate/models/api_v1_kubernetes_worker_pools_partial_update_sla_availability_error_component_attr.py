from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_kubernetes_worker_pools_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
