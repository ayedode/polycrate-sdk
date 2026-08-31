from typing import Literal

ApiV1WorkspacesReloadCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_WORKSPACES_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_workspaces_reload_create_annotations_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateAnnotationsErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
