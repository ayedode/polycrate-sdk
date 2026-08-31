from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "required"
]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_workspaces_run_discovery_create_organization_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateOrganizationIdErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
