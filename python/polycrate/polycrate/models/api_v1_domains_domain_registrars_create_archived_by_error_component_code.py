from typing import Literal

ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domain_registrars_create_archived_by_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateArchivedByErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
