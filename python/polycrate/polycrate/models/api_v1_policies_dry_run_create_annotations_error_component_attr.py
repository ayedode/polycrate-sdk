from typing import Literal

ApiV1PoliciesDryRunCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_POLICIES_DRY_RUN_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_policies_dry_run_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateAnnotationsErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
