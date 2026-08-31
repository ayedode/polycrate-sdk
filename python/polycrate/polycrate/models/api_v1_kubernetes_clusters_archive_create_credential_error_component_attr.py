from typing import Literal

ApiV1KubernetesClustersArchiveCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_kubernetes_clusters_archive_create_credential_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateCredentialErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
