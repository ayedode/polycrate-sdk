from typing import Literal

ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponentAttr = Literal["auth_code_credential_id"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_AUTH_CODE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponentAttr
] = {
    "auth_code_credential_id",
}


def check_api_v1_domains_domains_archive_create_auth_code_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_AUTH_CODE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_AUTH_CODE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
