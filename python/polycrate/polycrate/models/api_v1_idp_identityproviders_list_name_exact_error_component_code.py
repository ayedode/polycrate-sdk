from typing import Literal

ApiV1IdpIdentityprovidersListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersListNameExactErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_idp_identityproviders_list_name_exact_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersListNameExactErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
