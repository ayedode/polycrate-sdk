from typing import Literal

ApiV1KubernetesClustersPartialUpdateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_clusters_partial_update_credential_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateCredentialErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
