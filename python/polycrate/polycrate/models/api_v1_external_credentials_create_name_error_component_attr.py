from typing import Literal

ApiV1ExternalCredentialsCreateNameErrorComponentAttr = Literal["name"]

API_V1_EXTERNAL_CREDENTIALS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ExternalCredentialsCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_external_credentials_create_name_error_component_attr(
    value: str,
) -> ApiV1ExternalCredentialsCreateNameErrorComponentAttr:
    if value in API_V1_EXTERNAL_CREDENTIALS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_EXTERNAL_CREDENTIALS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
