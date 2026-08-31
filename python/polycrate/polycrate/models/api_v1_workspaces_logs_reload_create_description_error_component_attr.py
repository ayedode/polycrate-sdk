from typing import Literal

ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspaces_logs_reload_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
