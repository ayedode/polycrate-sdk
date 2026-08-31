from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_worker_pools_partial_update_archived_reason_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
