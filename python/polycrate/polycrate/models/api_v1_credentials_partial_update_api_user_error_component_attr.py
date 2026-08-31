from typing import Literal

ApiV1CredentialsPartialUpdateApiUserErrorComponentAttr = Literal["api_user"]

API_V1_CREDENTIALS_PARTIAL_UPDATE_API_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsPartialUpdateApiUserErrorComponentAttr
] = {
    "api_user",
}


def check_api_v1_credentials_partial_update_api_user_error_component_attr(
    value: str,
) -> ApiV1CredentialsPartialUpdateApiUserErrorComponentAttr:
    if value in API_V1_CREDENTIALS_PARTIAL_UPDATE_API_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_PARTIAL_UPDATE_API_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
