from typing import Literal

ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponentAttr = Literal["operator_loglevel"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponentAttr
] = {
    "operator_loglevel",
}


def check_api_v1_kubernetes_clusters_partial_update_operator_loglevel_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateOperatorLoglevelErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
