from typing import Literal

ApiV1WorkspacesRepairCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_WORKSPACES_REPAIR_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_workspaces_repair_create_labels_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateLabelsErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
