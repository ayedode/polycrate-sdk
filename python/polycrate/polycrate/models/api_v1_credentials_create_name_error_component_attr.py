from typing import Literal

ApiV1CredentialsCreateNameErrorComponentAttr = Literal["name"]

API_V1_CREDENTIALS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_credentials_create_name_error_component_attr(
    value: str,
) -> ApiV1CredentialsCreateNameErrorComponentAttr:
    if value in API_V1_CREDENTIALS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
