from typing import Literal

ApiV1CredentialsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_credentials_create_kind_error_component_attr(
    value: str,
) -> ApiV1CredentialsCreateKindErrorComponentAttr:
    if value in API_V1_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
