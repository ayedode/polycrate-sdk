from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_kubernetes_worker_pools_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
