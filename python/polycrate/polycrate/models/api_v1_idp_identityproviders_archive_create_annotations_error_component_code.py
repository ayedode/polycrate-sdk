from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_idp_identityproviders_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
