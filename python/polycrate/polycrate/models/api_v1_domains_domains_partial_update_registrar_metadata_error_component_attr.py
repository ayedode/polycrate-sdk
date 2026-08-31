from typing import Literal

ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponentAttr = Literal["registrar_metadata"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponentAttr
] = {
    "registrar_metadata",
}


def check_api_v1_domains_domains_partial_update_registrar_metadata_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
