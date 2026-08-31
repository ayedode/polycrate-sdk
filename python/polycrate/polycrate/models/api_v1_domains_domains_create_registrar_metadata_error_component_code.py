from typing import Literal

ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAINS_CREATE_REGISTRAR_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domains_create_registrar_metadata_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_REGISTRAR_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_REGISTRAR_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
