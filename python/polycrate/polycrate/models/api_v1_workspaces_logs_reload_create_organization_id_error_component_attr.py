from typing import Literal

ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_workspaces_logs_reload_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
