from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_scm_repositories_partial_update_annotations_error_component import (
        ApiV1ScmRepositoriesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_archived_at_error_component import (
        ApiV1ScmRepositoriesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_archived_error_component import (
        ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_archived_reason_error_component import (
        ApiV1ScmRepositoriesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_credential_error_component import (
        ApiV1ScmRepositoriesPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_criticality_error_component import (
        ApiV1ScmRepositoriesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_debug_mode_error_component import (
        ApiV1ScmRepositoriesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_display_name_error_component import (
        ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_groups_count_error_component import (
        ApiV1ScmRepositoriesPartialUpdateGroupsCountErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_hostname_error_component import (
        ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_k8s_app_error_component import (
        ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_k8s_cluster_error_component import (
        ApiV1ScmRepositoriesPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_kind_error_component import (
        ApiV1ScmRepositoriesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_labels_error_component import (
        ApiV1ScmRepositoriesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_metadata_error_component import (
        ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_name_error_component import (
        ApiV1ScmRepositoriesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_non_field_errors_error_component import (
        ApiV1ScmRepositoriesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_platform_service_error_component import (
        ApiV1ScmRepositoriesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_projects_count_error_component import (
        ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_provider_error_component import (
        ApiV1ScmRepositoriesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_provider_id_error_component import (
        ApiV1ScmRepositoriesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_provider_reference_error_component import (
        ApiV1ScmRepositoriesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_reconciliation_enabled_error_component import (
        ApiV1ScmRepositoriesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_repository_version_error_component import (
        ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_sla_availability_error_component import (
        ApiV1ScmRepositoriesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_sla_target_error_component import (
        ApiV1ScmRepositoriesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_slo_availability_error_component import (
        ApiV1ScmRepositoriesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_slo_target_error_component import (
        ApiV1ScmRepositoriesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_target_availability_error_component import (
        ApiV1ScmRepositoriesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_tolerations_error_component import (
        ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_scm_repositories_partial_update_users_count_error_component import (
        ApiV1ScmRepositoriesPartialUpdateUsersCountErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ScmRepositoriesPartialUpdateValidationError")


@_attrs_define
class ApiV1ScmRepositoriesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ScmRepositoriesPartialUpdateAnnotationsErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateArchivedAtErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateArchivedReasonErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateCredentialErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateCriticalityErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateDebugModeErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateGroupsCountErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponent | ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponent
            | ApiV1ScmRepositoriesPartialUpdateK8SClusterErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateKindErrorComponent | ApiV1ScmRepositoriesPartialUpdateLabelsErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponent | ApiV1ScmRepositoriesPartialUpdateNameErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1ScmRepositoriesPartialUpdatePlatformServiceErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateProviderErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateProviderIdErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateProviderReferenceErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateSlaTargetErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateSloTargetErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponent |
            ApiV1ScmRepositoriesPartialUpdateUsersCountErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ScmRepositoriesPartialUpdateAnnotationsErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateArchivedAtErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateArchivedReasonErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateCredentialErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateCriticalityErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateDebugModeErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateGroupsCountErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateK8SClusterErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateKindErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateLabelsErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateNameErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ScmRepositoriesPartialUpdatePlatformServiceErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateProviderErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateProviderIdErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateProviderReferenceErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateSlaTargetErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateSloTargetErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponent
        | ApiV1ScmRepositoriesPartialUpdateUsersCountErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_scm_repositories_partial_update_annotations_error_component import (
            ApiV1ScmRepositoriesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_archived_at_error_component import (
            ApiV1ScmRepositoriesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_archived_error_component import (
            ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_archived_reason_error_component import (
            ApiV1ScmRepositoriesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_credential_error_component import (
            ApiV1ScmRepositoriesPartialUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_criticality_error_component import (
            ApiV1ScmRepositoriesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_debug_mode_error_component import (
            ApiV1ScmRepositoriesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_display_name_error_component import (
            ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_groups_count_error_component import (
            ApiV1ScmRepositoriesPartialUpdateGroupsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_hostname_error_component import (
            ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_k8s_app_error_component import (
            ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_k8s_cluster_error_component import (
            ApiV1ScmRepositoriesPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_kind_error_component import (
            ApiV1ScmRepositoriesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_labels_error_component import (
            ApiV1ScmRepositoriesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_name_error_component import (
            ApiV1ScmRepositoriesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_non_field_errors_error_component import (
            ApiV1ScmRepositoriesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_platform_service_error_component import (
            ApiV1ScmRepositoriesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_projects_count_error_component import (
            ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_provider_error_component import (
            ApiV1ScmRepositoriesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_provider_id_error_component import (
            ApiV1ScmRepositoriesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_provider_reference_error_component import (
            ApiV1ScmRepositoriesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_reconciliation_enabled_error_component import (
            ApiV1ScmRepositoriesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_repository_version_error_component import (
            ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_sla_availability_error_component import (
            ApiV1ScmRepositoriesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_sla_target_error_component import (
            ApiV1ScmRepositoriesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_slo_availability_error_component import (
            ApiV1ScmRepositoriesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_slo_target_error_component import (
            ApiV1ScmRepositoriesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_target_availability_error_component import (
            ApiV1ScmRepositoriesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_tolerations_error_component import (
            ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_users_count_error_component import (
            ApiV1ScmRepositoriesPartialUpdateUsersCountErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateUsersCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateGroupsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ScmRepositoriesPartialUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_scm_repositories_partial_update_annotations_error_component import (
            ApiV1ScmRepositoriesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_archived_at_error_component import (
            ApiV1ScmRepositoriesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_archived_error_component import (
            ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_archived_reason_error_component import (
            ApiV1ScmRepositoriesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_credential_error_component import (
            ApiV1ScmRepositoriesPartialUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_criticality_error_component import (
            ApiV1ScmRepositoriesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_debug_mode_error_component import (
            ApiV1ScmRepositoriesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_display_name_error_component import (
            ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_groups_count_error_component import (
            ApiV1ScmRepositoriesPartialUpdateGroupsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_hostname_error_component import (
            ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_k8s_app_error_component import (
            ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_k8s_cluster_error_component import (
            ApiV1ScmRepositoriesPartialUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_kind_error_component import (
            ApiV1ScmRepositoriesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_labels_error_component import (
            ApiV1ScmRepositoriesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_metadata_error_component import (
            ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_name_error_component import (
            ApiV1ScmRepositoriesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_non_field_errors_error_component import (
            ApiV1ScmRepositoriesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_platform_service_error_component import (
            ApiV1ScmRepositoriesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_projects_count_error_component import (
            ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_provider_error_component import (
            ApiV1ScmRepositoriesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_provider_id_error_component import (
            ApiV1ScmRepositoriesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_provider_reference_error_component import (
            ApiV1ScmRepositoriesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_reconciliation_enabled_error_component import (
            ApiV1ScmRepositoriesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_repository_version_error_component import (
            ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_sla_availability_error_component import (
            ApiV1ScmRepositoriesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_sla_target_error_component import (
            ApiV1ScmRepositoriesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_slo_availability_error_component import (
            ApiV1ScmRepositoriesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_slo_target_error_component import (
            ApiV1ScmRepositoriesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_target_availability_error_component import (
            ApiV1ScmRepositoriesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_tolerations_error_component import (
            ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_scm_repositories_partial_update_users_count_error_component import (
            ApiV1ScmRepositoriesPartialUpdateUsersCountErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ScmRepositoriesPartialUpdateAnnotationsErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateArchivedAtErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateArchivedReasonErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateCredentialErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateCriticalityErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateDebugModeErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateGroupsCountErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateK8SClusterErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateKindErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateLabelsErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateNameErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ScmRepositoriesPartialUpdatePlatformServiceErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateProviderErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateProviderIdErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateProviderReferenceErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateSlaTargetErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateSloTargetErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponent
                | ApiV1ScmRepositoriesPartialUpdateUsersCountErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_0 = (
                        ApiV1ScmRepositoriesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_1 = (
                        ApiV1ScmRepositoriesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_2 = (
                        ApiV1ScmRepositoriesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_3 = (
                        ApiV1ScmRepositoriesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_4 = (
                        ApiV1ScmRepositoriesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_5 = (
                        ApiV1ScmRepositoriesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_6 = (
                        ApiV1ScmRepositoriesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_7 = (
                        ApiV1ScmRepositoriesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_8 = (
                        ApiV1ScmRepositoriesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_9 = (
                        ApiV1ScmRepositoriesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_10 = (
                        ApiV1ScmRepositoriesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_11 = (
                        ApiV1ScmRepositoriesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_12 = (
                        ApiV1ScmRepositoriesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_13 = (
                        ApiV1ScmRepositoriesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_14 = (
                        ApiV1ScmRepositoriesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_15 = (
                        ApiV1ScmRepositoriesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_16 = (
                        ApiV1ScmRepositoriesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_17 = (
                        ApiV1ScmRepositoriesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_18 = (
                        ApiV1ScmRepositoriesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_19 = (
                        ApiV1ScmRepositoriesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_20 = (
                        ApiV1ScmRepositoriesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_21 = (
                        ApiV1ScmRepositoriesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_22 = (
                        ApiV1ScmRepositoriesPartialUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_23 = (
                        ApiV1ScmRepositoriesPartialUpdateProjectsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_24 = (
                        ApiV1ScmRepositoriesPartialUpdateUsersCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_25 = (
                        ApiV1ScmRepositoriesPartialUpdateGroupsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_26 = (
                        ApiV1ScmRepositoriesPartialUpdateRepositoryVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_27 = (
                        ApiV1ScmRepositoriesPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_28 = (
                        ApiV1ScmRepositoriesPartialUpdateK8SAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_scm_repositories_partial_update_error_type_29 = (
                        ApiV1ScmRepositoriesPartialUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_scm_repositories_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_scm_repositories_partial_update_error_type_30 = (
                    ApiV1ScmRepositoriesPartialUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_scm_repositories_partial_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_scm_repositories_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_scm_repositories_partial_update_validation_error.additional_properties = d
        return api_v1_scm_repositories_partial_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
