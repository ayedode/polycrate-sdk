from typing import Literal

ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_partial_update_created_by_user_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateCreatedByUserErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_CREATED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
