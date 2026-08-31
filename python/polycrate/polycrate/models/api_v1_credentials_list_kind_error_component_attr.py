from typing import Literal

ApiV1CredentialsListKindErrorComponentAttr = Literal["kind"]

API_V1_CREDENTIALS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_credentials_list_kind_error_component_attr(value: str) -> ApiV1CredentialsListKindErrorComponentAttr:
    if value in API_V1_CREDENTIALS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
