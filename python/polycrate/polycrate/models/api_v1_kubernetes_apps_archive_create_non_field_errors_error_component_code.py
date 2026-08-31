from typing import Literal

ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
