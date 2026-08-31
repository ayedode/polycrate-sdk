from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backup_schedules_partial_update_annotations_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_archived_at_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_archived_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_archived_reason_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_criticality_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_debug_mode_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_display_name_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_k8s_cluster_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_kind_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_labels_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_last_backup_at_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_metadata_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_name_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_non_field_errors_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_paused_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_platform_service_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_provider_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_provider_id_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_provider_reference_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_reconciliation_enabled_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_retention_policy_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateRetentionPolicyErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_schedule_cron_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateScheduleCronErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_sla_availability_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_sla_target_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_slo_availability_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_slo_target_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_source_namespace_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_status_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_target_availability_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_tolerations_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_partial_update_total_backups_error_component import (
        ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupSchedulesPartialUpdateValidationError")


@_attrs_define
class ApiV1BackupsBackupSchedulesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupSchedulesPartialUpdateAnnotationsErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedAtErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedReasonErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateCriticalityErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateDebugModeErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateDisplayNameErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateK8SClusterErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateKindErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateNameErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdatePlatformServiceErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateProviderReferenceErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateRetentionPolicyErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateScheduleCronErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateSloTargetErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateSourceNamespaceErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponent |
            ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupSchedulesPartialUpdateAnnotationsErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateArchivedAtErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateArchivedErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateArchivedReasonErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateCriticalityErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateDebugModeErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateDisplayNameErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateK8SClusterErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateKindErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateNameErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdatePlatformServiceErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateProviderReferenceErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateRetentionPolicyErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateScheduleCronErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateSloTargetErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateSourceNamespaceErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponent
        | ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backup_schedules_partial_update_annotations_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_archived_at_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_archived_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_archived_reason_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_criticality_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_debug_mode_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_display_name_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_kind_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_labels_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_last_backup_at_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_name_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_non_field_errors_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_paused_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_platform_service_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_provider_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_provider_id_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_provider_reference_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_retention_policy_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateRetentionPolicyErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_schedule_cron_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateScheduleCronErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_sla_availability_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_sla_target_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_slo_availability_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_slo_target_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSourceNamespaceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_status_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_target_availability_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_tolerations_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_total_backups_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateScheduleCronErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateRetentionPolicyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponent):
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
        from ..models.api_v1_backups_backup_schedules_partial_update_annotations_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_archived_at_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_archived_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_archived_reason_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_criticality_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_debug_mode_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_display_name_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateK8SClusterErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_kind_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_labels_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_last_backup_at_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_metadata_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_name_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_non_field_errors_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_paused_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_platform_service_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_provider_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_provider_id_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_provider_reference_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_retention_policy_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateRetentionPolicyErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_schedule_cron_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateScheduleCronErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_sla_availability_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_sla_target_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_slo_availability_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_slo_target_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateSourceNamespaceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_status_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_target_availability_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_tolerations_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_partial_update_total_backups_error_component import (
            ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupSchedulesPartialUpdateAnnotationsErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateArchivedAtErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateArchivedErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateArchivedReasonErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateCriticalityErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateDebugModeErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateDisplayNameErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateK8SClusterErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateKindErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateNameErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdatePlatformServiceErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateProviderReferenceErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateRetentionPolicyErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateScheduleCronErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateSloTargetErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateSourceNamespaceErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponent
                | ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_0 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_1 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_2 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_3 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_4 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_5 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_6 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_7 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_8 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_9 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_10 = (
                        ApiV1BackupsBackupSchedulesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_11 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_12 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_13 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_14 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_15 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_16 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_17 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_18 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_19 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_20 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_21 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_22 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_23 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_24 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_25 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateScheduleCronErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_26 = (
                        ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_27 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateRetentionPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_28 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_29 = (
                        ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_30 = (
                    ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backup_schedules_partial_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backup_schedules_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backup_schedules_partial_update_validation_error.additional_properties = d
        return api_v1_backups_backup_schedules_partial_update_validation_error

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
