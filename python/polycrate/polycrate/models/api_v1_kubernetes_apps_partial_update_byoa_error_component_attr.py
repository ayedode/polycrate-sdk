from typing import Literal

ApiV1KubernetesAppsPartialUpdateByoaErrorComponentAttr = Literal["byoa"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BYOA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateByoaErrorComponentAttr
] = {
    "byoa",
}


def check_api_v1_kubernetes_apps_partial_update_byoa_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateByoaErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BYOA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BYOA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
