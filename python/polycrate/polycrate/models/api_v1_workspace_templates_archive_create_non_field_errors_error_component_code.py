from typing import Literal

ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspace_templates_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1WorkspaceTemplatesArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
