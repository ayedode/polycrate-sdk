from typing import Literal

ApiV1WorkspacesRepairCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_WORKSPACES_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_workspaces_repair_create_annotations_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateAnnotationsErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
