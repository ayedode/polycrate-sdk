from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1_domains_domain_registrars_archive_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateCreatedByUserErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
