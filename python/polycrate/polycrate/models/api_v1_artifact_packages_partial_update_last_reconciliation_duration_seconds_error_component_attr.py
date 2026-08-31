from typing import Literal

ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponentAttr = Literal[
    "last_reconciliation_duration_seconds"
]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponentAttr
] = {
    "last_reconciliation_duration_seconds",
}


def check_api_v1_artifact_packages_partial_update_last_reconciliation_duration_seconds_error_component_attr(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdateLastReconciliationDurationSecondsErrorComponentAttr:
    if (
        value
        in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_LAST_RECONCILIATION_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
