from typing import Literal

ApiV1WorkspacesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_workspaces_create_annotations_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
