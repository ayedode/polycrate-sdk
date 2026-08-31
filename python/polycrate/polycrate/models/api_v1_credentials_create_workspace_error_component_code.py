from typing import Literal

ApiV1CredentialsCreateWorkspaceErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1_CREDENTIALS_CREATE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsCreateWorkspaceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_credentials_create_workspace_error_component_code(
    value: str,
) -> ApiV1CredentialsCreateWorkspaceErrorComponentCode:
    if value in API_V1_CREDENTIALS_CREATE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
