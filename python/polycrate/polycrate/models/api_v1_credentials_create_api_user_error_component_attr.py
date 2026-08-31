from typing import Literal

ApiV1CredentialsCreateApiUserErrorComponentAttr = Literal["api_user"]

API_V1_CREDENTIALS_CREATE_API_USER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsCreateApiUserErrorComponentAttr] = {
    "api_user",
}


def check_api_v1_credentials_create_api_user_error_component_attr(
    value: str,
) -> ApiV1CredentialsCreateApiUserErrorComponentAttr:
    if value in API_V1_CREDENTIALS_CREATE_API_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_API_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
