from typing import Literal

ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_create_powerdns_metadata_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
