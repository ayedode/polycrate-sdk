from typing import Literal

ApiV1WorkspacesCheckCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_WORKSPACES_CHECK_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_workspaces_check_create_annotations_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateAnnotationsErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
