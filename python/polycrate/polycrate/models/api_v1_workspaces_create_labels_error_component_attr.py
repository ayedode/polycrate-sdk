from typing import Literal

ApiV1WorkspacesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_WORKSPACES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesCreateLabelsErrorComponentAttr] = {
    "labels",
}


def check_api_v1_workspaces_create_labels_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateLabelsErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
