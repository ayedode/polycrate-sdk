from typing import Literal

CodeRepositoryListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

CODE_REPOSITORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[CodeRepositoryListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_code_repository_list_effective_criticality_type_1(value: str) -> CodeRepositoryListEffectiveCriticalityType1:
    if value in CODE_REPOSITORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
