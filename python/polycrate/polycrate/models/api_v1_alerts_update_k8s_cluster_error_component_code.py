from typing import Literal

ApiV1AlertsUpdateK8SClusterErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTS_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateK8SClusterErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alerts_update_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1AlertsUpdateK8SClusterErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
