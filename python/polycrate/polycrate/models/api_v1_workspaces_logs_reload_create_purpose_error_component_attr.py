from typing import Literal

ApiV1WorkspacesLogsReloadCreatePurposeErrorComponentAttr = Literal["purpose"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreatePurposeErrorComponentAttr
] = {
    "purpose",
}


def check_api_v1_workspaces_logs_reload_create_purpose_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreatePurposeErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PURPOSE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
