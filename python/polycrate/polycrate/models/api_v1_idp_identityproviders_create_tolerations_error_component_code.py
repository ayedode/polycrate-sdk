from typing import Literal

ApiV1IdpIdentityprovidersCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_idp_identityproviders_create_tolerations_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateTolerationsErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
