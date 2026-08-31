from typing import Literal

ApiV1KubernetesAddonsUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDONS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addons_update_archived_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsUpdateArchivedErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
