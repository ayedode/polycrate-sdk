from typing import Literal

ApiV1CredentialsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_CREDENTIALS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CredentialsListCreatedAtErrorComponentCode] = {
    "invalid",
}


def check_api_v1_credentials_list_created_at_error_component_code(
    value: str,
) -> ApiV1CredentialsListCreatedAtErrorComponentCode:
    if value in API_V1_CREDENTIALS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
