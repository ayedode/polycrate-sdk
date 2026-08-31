from typing import Literal

ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponentAttr = Literal["tech_contact_id"]

API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponentAttr
] = {
    "tech_contact_id",
}


def check_api_v1_domains_domains_archive_create_tech_contact_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_ARCHIVE_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
