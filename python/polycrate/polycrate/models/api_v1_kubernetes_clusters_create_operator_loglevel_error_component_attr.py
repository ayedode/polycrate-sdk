from typing import Literal

ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponentAttr = Literal["operator_loglevel"]

API_V1_KUBERNETES_CLUSTERS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponentAttr
] = {
    "operator_loglevel",
}


def check_api_v1_kubernetes_clusters_create_operator_loglevel_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersCreateOperatorLoglevelErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
