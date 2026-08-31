from typing import Literal

ApiV1DomainsDomainsCreateRegistrarIdErrorComponentAttr = Literal["registrar_id"]

API_V1_DOMAINS_DOMAINS_CREATE_REGISTRAR_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateRegistrarIdErrorComponentAttr
] = {
    "registrar_id",
}


def check_api_v1_domains_domains_create_registrar_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateRegistrarIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_REGISTRAR_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_REGISTRAR_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
