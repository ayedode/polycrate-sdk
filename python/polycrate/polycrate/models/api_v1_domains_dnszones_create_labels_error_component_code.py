from typing import Literal

ApiV1DomainsDnszonesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_create_labels_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesCreateLabelsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
