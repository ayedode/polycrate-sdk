from typing import Literal

ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1_WORKSPACES_DISCOVER_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_workspaces_discover_create_organization_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateOrganizationIdErrorComponentCode:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
