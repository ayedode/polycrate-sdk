from typing import Literal

ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_partial_update_operator_loglevel_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
