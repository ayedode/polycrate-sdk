from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_idp_identityproviders_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
