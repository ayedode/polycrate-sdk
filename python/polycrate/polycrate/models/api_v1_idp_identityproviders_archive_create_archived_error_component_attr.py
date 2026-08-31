from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_idp_identityproviders_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
