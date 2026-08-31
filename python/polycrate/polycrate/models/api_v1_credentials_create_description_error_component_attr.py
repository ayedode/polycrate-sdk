from typing import Literal

ApiV1CredentialsCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_CREDENTIALS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_credentials_create_description_error_component_attr(
    value: str,
) -> ApiV1CredentialsCreateDescriptionErrorComponentAttr:
    if value in API_V1_CREDENTIALS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
