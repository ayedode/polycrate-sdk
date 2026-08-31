from typing import Literal

ApiV1IdpIdentityprovidersCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_idp_identityproviders_create_labels_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateLabelsErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
