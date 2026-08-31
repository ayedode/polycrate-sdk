from typing import Literal

ApiV1KubernetesAppsCreateByoaErrorComponentAttr = Literal["byoa"]

API_V1_KUBERNETES_APPS_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1KubernetesAppsCreateByoaErrorComponentAttr] = {
    "byoa",
}


def check_api_v1_kubernetes_apps_create_byoa_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateByoaErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_BYOA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
