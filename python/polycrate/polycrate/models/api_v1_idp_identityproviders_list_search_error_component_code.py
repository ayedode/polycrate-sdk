from typing import Literal

ApiV1IdpIdentityprovidersListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_idp_identityproviders_list_search_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersListSearchErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
