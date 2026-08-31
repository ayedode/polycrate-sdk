from typing import Literal

ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "unique"
]

API_V1_KUBERNETES_CLUSTERS_UPDATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "unique",
}


def check_api_v1_kubernetes_clusters_update_gitlab_project_id_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateGitlabProjectIdErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
