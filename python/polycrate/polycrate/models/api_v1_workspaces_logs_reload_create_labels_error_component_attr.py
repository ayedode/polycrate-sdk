from typing import Literal

ApiV1WorkspacesLogsReloadCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_workspaces_logs_reload_create_labels_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateLabelsErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
