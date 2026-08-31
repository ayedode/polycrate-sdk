from typing import Literal

ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponentAttr = Literal["registrar_id"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponentAttr
] = {
    "registrar_id",
}


def check_api_v1_domains_domains_partial_update_registrar_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateRegistrarIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_REGISTRAR_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
