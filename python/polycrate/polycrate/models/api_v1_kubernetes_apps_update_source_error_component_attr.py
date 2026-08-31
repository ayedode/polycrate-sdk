from typing import Literal

ApiV1KubernetesAppsUpdateSourceErrorComponentAttr = Literal["source"]

API_V1_KUBERNETES_APPS_UPDATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateSourceErrorComponentAttr
] = {
    "source",
}


def check_api_v1_kubernetes_apps_update_source_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateSourceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
