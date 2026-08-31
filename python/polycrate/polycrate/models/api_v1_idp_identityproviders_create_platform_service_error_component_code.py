from typing import Literal

ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_idp_identityproviders_create_platform_service_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersCreatePlatformServiceErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
