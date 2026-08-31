from typing import Literal

ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponentAttr = Literal["gitlab_project_id"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponentAttr
] = {
    "gitlab_project_id",
}


def check_api_v1_kubernetes_clusters_discover_create_gitlab_project_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateGitlabProjectIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_GITLAB_PROJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
