from typing import Literal

ApiV1DowntimesListKubernetesAppsErrorComponentAttr = Literal["kubernetes_apps"]

API_V1_DOWNTIMES_LIST_KUBERNETES_APPS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesListKubernetesAppsErrorComponentAttr
] = {
    "kubernetes_apps",
}


def check_api_v1_downtimes_list_kubernetes_apps_error_component_attr(
    value: str,
) -> ApiV1DowntimesListKubernetesAppsErrorComponentAttr:
    if value in API_V1_DOWNTIMES_LIST_KUBERNETES_APPS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_KUBERNETES_APPS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
