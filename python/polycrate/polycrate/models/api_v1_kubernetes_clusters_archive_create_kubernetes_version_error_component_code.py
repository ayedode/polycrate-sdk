from typing import Literal

ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_KUBERNETES_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_clusters_archive_create_kubernetes_version_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateKubernetesVersionErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_KUBERNETES_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_KUBERNETES_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
