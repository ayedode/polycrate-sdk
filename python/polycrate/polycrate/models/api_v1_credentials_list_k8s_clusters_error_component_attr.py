from typing import Literal

ApiV1CredentialsListK8SClustersErrorComponentAttr = Literal["k8s_clusters"]

API_V1_CREDENTIALS_LIST_K8S_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsListK8SClustersErrorComponentAttr
] = {
    "k8s_clusters",
}


def check_api_v1_credentials_list_k8s_clusters_error_component_attr(
    value: str,
) -> ApiV1CredentialsListK8SClustersErrorComponentAttr:
    if value in API_V1_CREDENTIALS_LIST_K8S_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_K8S_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
