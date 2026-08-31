from typing import Literal

ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponentAttr = Literal["is_default"]

API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponentAttr
] = {
    "is_default",
}


def check_api_v1_workspace_templates_archive_create_is_default_error_component_attr(
    value: str,
) -> ApiV1WorkspaceTemplatesArchiveCreateIsDefaultErrorComponentAttr:
    if value in API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACE_TEMPLATES_ARCHIVE_CREATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
