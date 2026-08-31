from typing import Literal

ApiV1PoliciesDryRunCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_POLICIES_DRY_RUN_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_policies_dry_run_create_annotations_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateAnnotationsErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
