from typing import Literal

ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_DISCOVER_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_discover_create_on_premise_error_component_code(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateOnPremiseErrorComponentCode:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_ON_PREMISE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
