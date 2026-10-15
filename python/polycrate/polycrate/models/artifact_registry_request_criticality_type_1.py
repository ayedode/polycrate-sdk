from typing import Literal

ArtifactRegistryRequestCriticalityType1 = Literal["", "high", "low", "medium"]

ARTIFACT_REGISTRY_REQUEST_CRITICALITY_TYPE_1_VALUES: set[ArtifactRegistryRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_artifact_registry_request_criticality_type_1(value: str) -> ArtifactRegistryRequestCriticalityType1:
    if value in ARTIFACT_REGISTRY_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REGISTRY_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
