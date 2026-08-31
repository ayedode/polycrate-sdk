from typing import Literal

ApiV1CredentialsListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_CREDENTIALS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CredentialsListNameErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_credentials_list_name_error_component_code(value: str) -> ApiV1CredentialsListNameErrorComponentCode:
    if value in API_V1_CREDENTIALS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
