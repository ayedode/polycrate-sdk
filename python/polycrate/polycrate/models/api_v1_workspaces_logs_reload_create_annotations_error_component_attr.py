from typing import Literal

ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_workspaces_logs_reload_create_annotations_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateAnnotationsErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
