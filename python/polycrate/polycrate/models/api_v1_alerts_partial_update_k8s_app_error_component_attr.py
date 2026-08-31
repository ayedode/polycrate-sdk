from typing import Literal

ApiV1AlertsPartialUpdateK8SAppErrorComponentAttr = Literal["k8s_app"]

API_V1_ALERTS_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateK8SAppErrorComponentAttr
] = {
    "k8s_app",
}


def check_api_v1_alerts_partial_update_k8s_app_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateK8SAppErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
