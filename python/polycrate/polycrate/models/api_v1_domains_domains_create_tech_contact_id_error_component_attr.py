from typing import Literal

ApiV1DomainsDomainsCreateTechContactIdErrorComponentAttr = Literal["tech_contact_id"]

API_V1_DOMAINS_DOMAINS_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateTechContactIdErrorComponentAttr
] = {
    "tech_contact_id",
}


def check_api_v1_domains_domains_create_tech_contact_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateTechContactIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
