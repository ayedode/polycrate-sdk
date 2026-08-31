from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domain_registrars_archive_create_api_credential_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
