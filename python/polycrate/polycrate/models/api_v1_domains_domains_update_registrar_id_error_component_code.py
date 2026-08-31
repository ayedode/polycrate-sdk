from typing import Literal

ApiV1DomainsDomainsUpdateRegistrarIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null"]

API_V1_DOMAINS_DOMAINS_UPDATE_REGISTRAR_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsUpdateRegistrarIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
}


def check_api_v1_domains_domains_update_registrar_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsUpdateRegistrarIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_REGISTRAR_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_REGISTRAR_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
