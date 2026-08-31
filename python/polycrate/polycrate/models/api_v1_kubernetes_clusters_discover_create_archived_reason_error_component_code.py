from typing import Literal

ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_clusters_discover_create_archived_reason_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateArchivedReasonErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
