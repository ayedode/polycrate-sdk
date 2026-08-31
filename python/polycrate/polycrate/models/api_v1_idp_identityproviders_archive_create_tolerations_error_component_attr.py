from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_idp_identityproviders_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
