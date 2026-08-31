from typing import Literal

ApiV1DomainsDomainsCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOMAINS_DOMAINS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_domains_domains_create_labels_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateLabelsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
