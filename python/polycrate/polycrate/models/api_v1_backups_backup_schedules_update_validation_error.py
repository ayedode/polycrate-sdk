from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backup_schedules_update_annotations_error_component import (
        ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_archived_at_error_component import (
        ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_archived_error_component import (
        ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_archived_reason_error_component import (
        ApiV1BackupsBackupSchedulesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_criticality_error_component import (
        ApiV1BackupsBackupSchedulesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_debug_mode_error_component import (
        ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_display_name_error_component import (
        ApiV1BackupsBackupSchedulesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_k8s_cluster_error_component import (
        ApiV1BackupsBackupSchedulesUpdateK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_kind_error_component import (
        ApiV1BackupsBackupSchedulesUpdateKindErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_labels_error_component import (
        ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_last_backup_at_error_component import (
        ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_metadata_error_component import (
        ApiV1BackupsBackupSchedulesUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_name_error_component import (
        ApiV1BackupsBackupSchedulesUpdateNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_non_field_errors_error_component import (
        ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_paused_error_component import (
        ApiV1BackupsBackupSchedulesUpdatePausedErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_platform_service_error_component import (
        ApiV1BackupsBackupSchedulesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_provider_error_component import (
        ApiV1BackupsBackupSchedulesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_provider_id_error_component import (
        ApiV1BackupsBackupSchedulesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_provider_reference_error_component import (
        ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_reconciliation_enabled_error_component import (
        ApiV1BackupsBackupSchedulesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_retention_policy_error_component import (
        ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_schedule_cron_error_component import (
        ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_sla_availability_error_component import (
        ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_sla_target_error_component import (
        ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_slo_availability_error_component import (
        ApiV1BackupsBackupSchedulesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_slo_target_error_component import (
        ApiV1BackupsBackupSchedulesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_source_namespace_error_component import (
        ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_status_error_component import (
        ApiV1BackupsBackupSchedulesUpdateStatusErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_target_availability_error_component import (
        ApiV1BackupsBackupSchedulesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_tolerations_error_component import (
        ApiV1BackupsBackupSchedulesUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_update_total_backups_error_component import (
        ApiV1BackupsBackupSchedulesUpdateTotalBackupsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupSchedulesUpdateValidationError")


@_attrs_define
class ApiV1BackupsBackupSchedulesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateArchivedReasonErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateCriticalityErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateDisplayNameErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateK8SClusterErrorComponent | ApiV1BackupsBackupSchedulesUpdateKindErrorComponent
            | ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateMetadataErrorComponent | ApiV1BackupsBackupSchedulesUpdateNameErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponent |
            ApiV1BackupsBackupSchedulesUpdatePausedErrorComponent |
            ApiV1BackupsBackupSchedulesUpdatePlatformServiceErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateProviderErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateProviderIdErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateReconciliationEnabledErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateSloAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateSloTargetErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateStatusErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateTargetAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateTolerationsErrorComponent |
            ApiV1BackupsBackupSchedulesUpdateTotalBackupsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateArchivedReasonErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateCriticalityErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateDisplayNameErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateK8SClusterErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateKindErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateMetadataErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateNameErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponent
        | ApiV1BackupsBackupSchedulesUpdatePausedErrorComponent
        | ApiV1BackupsBackupSchedulesUpdatePlatformServiceErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateProviderErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateProviderIdErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateReconciliationEnabledErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateSloAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateSloTargetErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateStatusErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateTargetAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateTolerationsErrorComponent
        | ApiV1BackupsBackupSchedulesUpdateTotalBackupsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backup_schedules_update_annotations_error_component import (
            ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_archived_at_error_component import (
            ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_archived_error_component import (
            ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_archived_reason_error_component import (
            ApiV1BackupsBackupSchedulesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_criticality_error_component import (
            ApiV1BackupsBackupSchedulesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_debug_mode_error_component import (
            ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_display_name_error_component import (
            ApiV1BackupsBackupSchedulesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_kind_error_component import (
            ApiV1BackupsBackupSchedulesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_labels_error_component import (
            ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_last_backup_at_error_component import (
            ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_name_error_component import (
            ApiV1BackupsBackupSchedulesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_non_field_errors_error_component import (
            ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_paused_error_component import (
            ApiV1BackupsBackupSchedulesUpdatePausedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_platform_service_error_component import (
            ApiV1BackupsBackupSchedulesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_provider_error_component import (
            ApiV1BackupsBackupSchedulesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_provider_id_error_component import (
            ApiV1BackupsBackupSchedulesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_provider_reference_error_component import (
            ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupSchedulesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_retention_policy_error_component import (
            ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_schedule_cron_error_component import (
            ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_sla_availability_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_sla_target_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_slo_availability_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_slo_target_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_status_error_component import (
            ApiV1BackupsBackupSchedulesUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_target_availability_error_component import (
            ApiV1BackupsBackupSchedulesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_tolerations_error_component import (
            ApiV1BackupsBackupSchedulesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_total_backups_error_component import (
            ApiV1BackupsBackupSchedulesUpdateTotalBackupsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdatePausedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesUpdateTotalBackupsErrorComponent):
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
        from ..models.api_v1_backups_backup_schedules_update_annotations_error_component import (
            ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_archived_at_error_component import (
            ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_archived_error_component import (
            ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_archived_reason_error_component import (
            ApiV1BackupsBackupSchedulesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_criticality_error_component import (
            ApiV1BackupsBackupSchedulesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_debug_mode_error_component import (
            ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_display_name_error_component import (
            ApiV1BackupsBackupSchedulesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesUpdateK8SClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_kind_error_component import (
            ApiV1BackupsBackupSchedulesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_labels_error_component import (
            ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_last_backup_at_error_component import (
            ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_metadata_error_component import (
            ApiV1BackupsBackupSchedulesUpdateMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_name_error_component import (
            ApiV1BackupsBackupSchedulesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_non_field_errors_error_component import (
            ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_paused_error_component import (
            ApiV1BackupsBackupSchedulesUpdatePausedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_platform_service_error_component import (
            ApiV1BackupsBackupSchedulesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_provider_error_component import (
            ApiV1BackupsBackupSchedulesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_provider_id_error_component import (
            ApiV1BackupsBackupSchedulesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_provider_reference_error_component import (
            ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupSchedulesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_retention_policy_error_component import (
            ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_schedule_cron_error_component import (
            ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_sla_availability_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_sla_target_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_slo_availability_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_slo_target_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_status_error_component import (
            ApiV1BackupsBackupSchedulesUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_target_availability_error_component import (
            ApiV1BackupsBackupSchedulesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_tolerations_error_component import (
            ApiV1BackupsBackupSchedulesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_backups_backup_schedules_update_total_backups_error_component import (
            ApiV1BackupsBackupSchedulesUpdateTotalBackupsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateArchivedReasonErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateCriticalityErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateDisplayNameErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateK8SClusterErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateKindErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateMetadataErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateNameErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponent
                | ApiV1BackupsBackupSchedulesUpdatePausedErrorComponent
                | ApiV1BackupsBackupSchedulesUpdatePlatformServiceErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateProviderErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateProviderIdErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateReconciliationEnabledErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateSloAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateSloTargetErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateStatusErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateTargetAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateTolerationsErrorComponent
                | ApiV1BackupsBackupSchedulesUpdateTotalBackupsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_0 = (
                        ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_1 = (
                        ApiV1BackupsBackupSchedulesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_2 = (
                        ApiV1BackupsBackupSchedulesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_3 = (
                        ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_4 = (
                        ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_5 = (
                        ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_6 = (
                        ApiV1BackupsBackupSchedulesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_7 = (
                        ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_8 = (
                        ApiV1BackupsBackupSchedulesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_9 = (
                        ApiV1BackupsBackupSchedulesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_10 = (
                        ApiV1BackupsBackupSchedulesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_11 = (
                        ApiV1BackupsBackupSchedulesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_12 = (
                        ApiV1BackupsBackupSchedulesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_13 = (
                        ApiV1BackupsBackupSchedulesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_14 = (
                        ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_15 = (
                        ApiV1BackupsBackupSchedulesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_16 = (
                        ApiV1BackupsBackupSchedulesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_17 = (
                        ApiV1BackupsBackupSchedulesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_18 = (
                        ApiV1BackupsBackupSchedulesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_19 = (
                        ApiV1BackupsBackupSchedulesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_20 = (
                        ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_21 = (
                        ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_22 = (
                        ApiV1BackupsBackupSchedulesUpdateSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_23 = (
                        ApiV1BackupsBackupSchedulesUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_24 = (
                        ApiV1BackupsBackupSchedulesUpdateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_25 = (
                        ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_26 = (
                        ApiV1BackupsBackupSchedulesUpdatePausedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_27 = (
                        ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_28 = (
                        ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_update_error_type_29 = (
                        ApiV1BackupsBackupSchedulesUpdateTotalBackupsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backup_schedules_update_error_type_30 = (
                    ApiV1BackupsBackupSchedulesUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backup_schedules_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backup_schedules_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backup_schedules_update_validation_error.additional_properties = d
        return api_v1_backups_backup_schedules_update_validation_error

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
