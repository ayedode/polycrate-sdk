from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_idp_identityproviders_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateNameErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
