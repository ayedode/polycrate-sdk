from typing import Literal

ApiV1CredentialsCreateWorkspaceErrorComponentAttr = Literal["workspace"]

API_V1_CREDENTIALS_CREATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsCreateWorkspaceErrorComponentAttr
] = {
    "workspace",
}


def check_api_v1_credentials_create_workspace_error_component_attr(
    value: str,
) -> ApiV1CredentialsCreateWorkspaceErrorComponentAttr:
    if value in API_V1_CREDENTIALS_CREATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
