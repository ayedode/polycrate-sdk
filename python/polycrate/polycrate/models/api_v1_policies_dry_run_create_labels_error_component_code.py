from typing import Literal

ApiV1PoliciesDryRunCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_POLICIES_DRY_RUN_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_policies_dry_run_create_labels_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateLabelsErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
