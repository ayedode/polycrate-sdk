from typing import Literal

ApiV1WorkspacesArchiveCreateTemplateErrorComponentCode = Literal["does_not_exist", "invalid"]

API_V1_WORKSPACES_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesArchiveCreateTemplateErrorComponentCode
] = {
    "does_not_exist",
    "invalid",
}


def check_api_v1_workspaces_archive_create_template_error_component_code(
    value: str,
) -> ApiV1WorkspacesArchiveCreateTemplateErrorComponentCode:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_TEMPLATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
