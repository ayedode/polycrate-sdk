from typing import Literal

ApiV1CredentialsListSearchErrorComponentAttr = Literal["search"]

API_V1_CREDENTIALS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CredentialsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_credentials_list_search_error_component_attr(
    value: str,
) -> ApiV1CredentialsListSearchErrorComponentAttr:
    if value in API_V1_CREDENTIALS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
