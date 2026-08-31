from typing import Literal

ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponentAttr = Literal["powerdns_metadata"]

API_V1_DOMAINS_DNSZONES_UPDATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponentAttr
] = {
    "powerdns_metadata",
}


def check_api_v1_domains_dnszones_update_powerdns_metadata_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdatePowerdnsMetadataErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
