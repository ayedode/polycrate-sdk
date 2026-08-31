from typing import Literal

ApiV1CredentialsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_CREDENTIALS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsListUpdatedAtErrorComponentAttr] = {
    "updated_at",
}


def check_api_v1_credentials_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1CredentialsListUpdatedAtErrorComponentAttr:
    if value in API_V1_CREDENTIALS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
