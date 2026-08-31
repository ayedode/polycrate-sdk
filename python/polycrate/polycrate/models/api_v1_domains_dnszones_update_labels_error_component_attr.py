from typing import Literal

ApiV1DomainsDnszonesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOMAINS_DNSZONES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_domains_dnszones_update_labels_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateLabelsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
