from typing import Literal

ApiV1WorkspacesCheckCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_CHECK_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_check_create_provider_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateProviderErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
