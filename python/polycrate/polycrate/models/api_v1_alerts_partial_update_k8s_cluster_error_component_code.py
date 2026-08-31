from typing import Literal

ApiV1AlertsPartialUpdateK8SClusterErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTS_PARTIAL_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertsPartialUpdateK8SClusterErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alerts_partial_update_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1AlertsPartialUpdateK8SClusterErrorComponentCode:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
