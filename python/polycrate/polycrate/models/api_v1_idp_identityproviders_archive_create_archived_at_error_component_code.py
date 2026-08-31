from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_idp_identityproviders_archive_create_archived_at_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateArchivedAtErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
