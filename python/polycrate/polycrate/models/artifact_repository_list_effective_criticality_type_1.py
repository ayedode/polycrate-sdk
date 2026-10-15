from typing import Literal

ArtifactRepositoryListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ARTIFACT_REPOSITORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ArtifactRepositoryListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_artifact_repository_list_effective_criticality_type_1(
    value: str,
) -> ArtifactRepositoryListEffectiveCriticalityType1:
    if value in ARTIFACT_REPOSITORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ARTIFACT_REPOSITORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
