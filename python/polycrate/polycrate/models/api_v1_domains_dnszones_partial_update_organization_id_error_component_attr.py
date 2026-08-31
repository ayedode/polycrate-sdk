from typing import Literal

ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_domains_dnszones_partial_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
