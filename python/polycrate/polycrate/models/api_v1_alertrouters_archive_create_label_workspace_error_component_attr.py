from typing import Literal

ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponentAttr = Literal["label_workspace"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponentAttr
] = {
    "label_workspace",
}


def check_api_v1_alertrouters_archive_create_label_workspace_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateLabelWorkspaceErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
