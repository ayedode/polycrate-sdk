from typing import Literal

ApiV1PoliciesDryRunCreateModelsSelectorErrorComponentAttr = Literal["models_selector"]

API_V1_POLICIES_DRY_RUN_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateModelsSelectorErrorComponentAttr
] = {
    "models_selector",
}


def check_api_v1_policies_dry_run_create_models_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateModelsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_MODELS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
