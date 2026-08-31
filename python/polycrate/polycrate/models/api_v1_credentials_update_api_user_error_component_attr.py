from typing import Literal

ApiV1CredentialsUpdateApiUserErrorComponentAttr = Literal["api_user"]

API_V1_CREDENTIALS_UPDATE_API_USER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsUpdateApiUserErrorComponentAttr] = {
    "api_user",
}


def check_api_v1_credentials_update_api_user_error_component_attr(
    value: str,
) -> ApiV1CredentialsUpdateApiUserErrorComponentAttr:
    if value in API_V1_CREDENTIALS_UPDATE_API_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_UPDATE_API_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
