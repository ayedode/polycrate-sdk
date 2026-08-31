from typing import Literal

ApiV1KubernetesAppsPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_apps_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateKindErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
