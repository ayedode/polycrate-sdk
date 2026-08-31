from typing import Literal

ApiV1RegionsListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_REGIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsListWorkspacesErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_regions_list_workspaces_error_component_code(
    value: str,
) -> ApiV1RegionsListWorkspacesErrorComponentCode:
    if value in API_V1_REGIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
