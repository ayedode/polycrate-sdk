from typing import Literal

ApiV1KubernetesAppsCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_KUBERNETES_APPS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_kubernetes_apps_create_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateSloWindowDaysErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
