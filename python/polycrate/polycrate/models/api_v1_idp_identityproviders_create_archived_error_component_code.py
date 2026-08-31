from typing import Literal

ApiV1IdpIdentityprovidersCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_idp_identityproviders_create_archived_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateArchivedErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
