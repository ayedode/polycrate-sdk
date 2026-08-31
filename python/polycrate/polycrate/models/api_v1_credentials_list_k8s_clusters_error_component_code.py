from typing import Literal

ApiV1CredentialsListK8SClustersErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_CREDENTIALS_LIST_K8S_CLUSTERS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsListK8SClustersErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_credentials_list_k8s_clusters_error_component_code(
    value: str,
) -> ApiV1CredentialsListK8SClustersErrorComponentCode:
    if value in API_V1_CREDENTIALS_LIST_K8S_CLUSTERS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_K8S_CLUSTERS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
