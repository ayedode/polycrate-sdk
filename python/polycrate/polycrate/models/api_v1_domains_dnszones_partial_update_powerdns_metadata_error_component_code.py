from typing import Literal

ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_partial_update_powerdns_metadata_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdatePowerdnsMetadataErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_POWERDNS_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
