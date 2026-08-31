from typing import Literal

ApiV1DomainsDnszonesListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_DOMAINS_DNSZONES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DomainsDnszonesListNameErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_domains_dnszones_list_name_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesListNameErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
