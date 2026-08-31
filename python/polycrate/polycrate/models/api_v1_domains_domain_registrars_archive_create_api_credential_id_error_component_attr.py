from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponentAttr = Literal["api_credential_id"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponentAttr
] = {
    "api_credential_id",
}


def check_api_v1_domains_domain_registrars_archive_create_api_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateApiCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
