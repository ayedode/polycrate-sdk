from typing import Literal

ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_idp_identityproviders_update_annotations_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
