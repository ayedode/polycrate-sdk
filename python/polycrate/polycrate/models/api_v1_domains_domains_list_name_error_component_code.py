from typing import Literal

ApiV1DomainsDomainsListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_DOMAINS_DOMAINS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DomainsDomainsListNameErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_domains_domains_list_name_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsListNameErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
