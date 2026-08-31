from typing import Literal

ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_OWNER_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domains_archive_create_owner_contact_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_OWNER_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_OWNER_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
