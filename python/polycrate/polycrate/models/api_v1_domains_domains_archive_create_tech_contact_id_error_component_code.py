from typing import Literal

ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domains_archive_create_tech_contact_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
