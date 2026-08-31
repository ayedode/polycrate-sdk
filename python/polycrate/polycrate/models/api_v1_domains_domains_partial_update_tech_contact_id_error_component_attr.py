from typing import Literal

ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponentAttr = Literal["tech_contact_id"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponentAttr
] = {
    "tech_contact_id",
}


def check_api_v1_domains_domains_partial_update_tech_contact_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateTechContactIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_TECH_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
