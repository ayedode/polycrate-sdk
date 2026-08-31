from typing import Literal

ApiV1KubernetesClustersListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_KUBERNETES_CLUSTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_kubernetes_clusters_list_organizations_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersListOrganizationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
