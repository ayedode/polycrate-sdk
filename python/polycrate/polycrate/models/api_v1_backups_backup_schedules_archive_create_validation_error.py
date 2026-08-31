from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_backups_backup_schedules_archive_create_annotations_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_archived_at_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_archived_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_archived_reason_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_criticality_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_debug_mode_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_display_name_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_k8s_cluster_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateK8SClusterErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_kind_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_labels_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_last_backup_at_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateLastBackupAtErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_metadata_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateMetadataErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_name_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_non_field_errors_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_paused_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_platform_service_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_provider_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_provider_id_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_provider_reference_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_reconciliation_enabled_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_retention_policy_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_schedule_cron_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_sla_availability_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_sla_target_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_slo_availability_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_slo_target_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_source_namespace_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateSourceNamespaceErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_status_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_target_availability_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_tolerations_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_backups_backup_schedules_archive_create_total_backups_error_component import (
        ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BackupsBackupSchedulesArchiveCreateValidationError")


@_attrs_define
class ApiV1BackupsBackupSchedulesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateCriticalityErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateDebugModeErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateDisplayNameErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateK8SClusterErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateKindErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateLastBackupAtErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateMetadataErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateProviderIdErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateProviderReferenceErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateSlaTargetErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateSloTargetErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateSourceNamespaceErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponent |
            ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateArchivedErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateCriticalityErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateDebugModeErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateDisplayNameErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateK8SClusterErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateKindErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateLastBackupAtErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateMetadataErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateProviderIdErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateProviderReferenceErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateSlaTargetErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateSloTargetErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateSourceNamespaceErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponent
        | ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_backups_backup_schedules_archive_create_annotations_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_archived_at_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_archived_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_archived_reason_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_criticality_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_debug_mode_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_display_name_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_kind_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_labels_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_last_backup_at_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateLastBackupAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_name_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_non_field_errors_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_paused_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_platform_service_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_provider_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_provider_id_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_provider_reference_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_retention_policy_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_schedule_cron_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_sla_availability_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_sla_target_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_slo_availability_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_slo_target_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSourceNamespaceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_status_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_target_availability_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_tolerations_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_total_backups_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateSourceNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateK8SClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateLastBackupAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponent):
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
        from ..models.api_v1_backups_backup_schedules_archive_create_annotations_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_archived_at_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_archived_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_archived_reason_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_criticality_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_debug_mode_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_display_name_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_k8s_cluster_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateK8SClusterErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_kind_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_labels_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_last_backup_at_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateLastBackupAtErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_metadata_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateMetadataErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_name_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_non_field_errors_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_paused_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_platform_service_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_provider_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_provider_id_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_provider_reference_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_reconciliation_enabled_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_retention_policy_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_schedule_cron_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_sla_availability_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_sla_target_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_slo_availability_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_slo_target_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_source_namespace_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateSourceNamespaceErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_status_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_target_availability_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_tolerations_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_backups_backup_schedules_archive_create_total_backups_error_component import (
            ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateArchivedErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateCriticalityErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateDebugModeErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateDisplayNameErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateK8SClusterErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateKindErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateLastBackupAtErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateMetadataErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateProviderIdErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateProviderReferenceErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateSlaTargetErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateSloTargetErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateSourceNamespaceErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponent
                | ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_0 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_1 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_2 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_3 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_4 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_5 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_6 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_7 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_8 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_9 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_10 = (
                        ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_11 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_12 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_13 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_14 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_15 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_16 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_17 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_18 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_19 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_20 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_21 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_22 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateSourceNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_23 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_24 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateK8SClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_25 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_26 = (
                        ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_27 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_28 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateLastBackupAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_29 = (
                        ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_30 = (
                    ApiV1BackupsBackupSchedulesArchiveCreateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_backups_backup_schedules_archive_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_backups_backup_schedules_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_backups_backup_schedules_archive_create_validation_error.additional_properties = d
        return api_v1_backups_backup_schedules_archive_create_validation_error

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
