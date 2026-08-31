from typing import Literal

ApiV1KubernetesAppsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_APPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1KubernetesAppsUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_kubernetes_apps_update_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
