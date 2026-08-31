from typing import Literal

ApiV1WorkspacesLogsReloadCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_workspaces_logs_reload_create_provider_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateProviderErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
