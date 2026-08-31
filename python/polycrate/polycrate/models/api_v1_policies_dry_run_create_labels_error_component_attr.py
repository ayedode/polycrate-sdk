from typing import Literal

ApiV1PoliciesDryRunCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_POLICIES_DRY_RUN_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_policies_dry_run_create_labels_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateLabelsErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
