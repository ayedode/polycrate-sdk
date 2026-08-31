from typing import Literal

ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "unique"
]

API_V1_KUBERNETES_CLUSTERS_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "unique",
}


def check_api_v1_kubernetes_clusters_create_gitlab_project_id_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateGitlabProjectIdErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
