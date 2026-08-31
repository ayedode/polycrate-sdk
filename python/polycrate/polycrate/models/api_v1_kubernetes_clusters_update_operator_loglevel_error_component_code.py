from typing import Literal

ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_update_operator_loglevel_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateOperatorLoglevelErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
