from typing import Literal

ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domains_partial_update_registrar_metadata_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateRegistrarMetadataErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
