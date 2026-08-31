from typing import Literal

ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponentAttr = Literal["workspace_id"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponentAttr
] = {
    "workspace_id",
}


def check_api_v1_alertrouters_archive_create_workspace_id_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateWorkspaceIdErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_WORKSPACE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
