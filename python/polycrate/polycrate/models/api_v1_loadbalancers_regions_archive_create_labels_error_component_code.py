from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_loadbalancers_regions_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
