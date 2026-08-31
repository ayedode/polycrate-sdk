from typing import Literal

ApiV1WorkspacesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_WORKSPACES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_workspaces_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
