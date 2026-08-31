from typing import Literal

ApiV1CvesPartialUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_CVES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesPartialUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_cves_partial_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1CvesPartialUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_CVES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
