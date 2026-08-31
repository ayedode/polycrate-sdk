from typing import Literal

ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponentAttr = Literal["powerdns_metadata"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponentAttr
] = {
    "powerdns_metadata",
}


def check_api_v1_domains_dnszones_rectify_create_powerdns_metadata_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
